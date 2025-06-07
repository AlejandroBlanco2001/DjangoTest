from django.db import IntegrityError
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from tasksmanagement.api.task.permissions import CanManipulateTask
from tasksmanagement.models import Task
from rest_framework.request import Request
from tasksmanagement.serializers import DetailedTaskSerializer, CreateTaskSerializer, DetailedTaskLabelSerializer, CreateTaskLabelSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import QuerySet
from logging import getLogger
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers

logger = getLogger(__name__)

class TaskListCreateAPIView(ListCreateAPIView):
    """
    API View to list and create tasks
    """
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    def get_queryset(self) -> QuerySet[Task]:
        return Task.objects.user_tasks(self.request.user).order_by('title')

    def get(self, request: Request, *args, **kwargs) -> Response:
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = DetailedTaskSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)
    
    def post(self, request: Request, *args, **kwargs) -> Response:
        context = {
            "request": self.request,
        }

        serializer = CreateTaskSerializer(data=request.data, context=context)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'There was an error creating the task: One or more fields are missing'}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError as e:
            logger.error(f'Error creating task: {e}')
            return Response({'There was an error creating the task': 'Task already exists'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f'Error creating task: {e}')
            return Response({'There was an error creating the task, please try again later'}, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    API View to retrieve, update and delete a task
    """
    permission_classes = [IsAuthenticated, CanManipulateTask]
    serializer_class = DetailedTaskSerializer

    def get_object(self) -> Task:
        id = self.kwargs.get('pk')
        task = get_object_or_404(Task, id=id)
        self.check_object_permissions(self.request, task)
        return task

    def delete(self, request: Request, *args, **kwargs) -> Response:
        label = self.get_object()

        logger.info(f"Deleting label: {label.pk}")
        label.is_deleted = True
        label.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get(self, request: Request, *args, **kwargs) -> Response:
        task = self.get_object()

        serializer = DetailedTaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request: Request, *args, **kwargs) -> Response:
        task = self.get_object()

        serializer = CreateTaskSerializer(task, data=request.data, partial=True)

        try:
            if serializer.is_valid():
                serializer.update(task, request.data)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'There was an error updating the task: One or more fields are missing'}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError as e:
            logger.error(f'Error updating task: {e}')
            return Response({'There was an error updating the task': 'Task already exists'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f'Error updating task: {e}')
            return Response({'There was an error updating the task, please try again later'}, status=status.HTTP_400_BAD_REQUEST)


class TaskLabelListCreateAPIView(ListCreateAPIView):
    """
    API View to list and create labels for a task
    """
    permission_classes = [IsAuthenticated, CanManipulateTask]
    pagination_class = PageNumberPagination

    def get_queryset(self) -> QuerySet[Task]:
        return Task.objects.user_tasks(self.request.user).prefetch_related('label').order_by('title')
    
    def get(self, request: Request, *args, **kwargs) -> Response:
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = DetailedTaskLabelSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)
    
    def post(self, request: Request, *args, **kwargs) -> Response:
        context = {
            "request": self.request,
        }

        serializer = CreateTaskLabelSerializer(data=request.data, context=context, partial=True)

        try:
            if serializer.is_valid():
                serializer.save(validated_data=serializer.validated_data)
                return Response({'Task paired with label'}, status=status.HTTP_201_CREATED)
            else:
                logger.error(f'Error pairing label: {serializer.errors}')
                return Response({'There was an error pairing label: One or more fields are missing'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f'Error pairing label: {e}')
            if isinstance(e, serializers.ValidationError):
                return Response({'There was an error pairing label: ' + e.detail['label']}, status=status.HTTP_400_BAD_REQUEST)

            return Response({'There was an error pairing label, please try again later'}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request: Request, *args, **kwargs) -> Response:
        task = self.get_object()
        label = self.kwargs.get('label_pk')

        logger.info(f"Deleting label: {label.pk}")
        task.label.remove(label)
        task.save()
        return Response(status=status.HTTP_204_NO_CONTENT)