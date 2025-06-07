from django.db import IntegrityError
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from tasksmanagement.api.task.permissions import CanManipulateTask
from tasksmanagement.models import Task
from rest_framework.request import Request
from tasksmanagement.serializers import DetailedTaskSerializer, CreateTaskSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import QuerySet
from logging import getLogger
from django.shortcuts import get_object_or_404


logger = getLogger(__name__)

class TaskListCreateAPIView(ListCreateAPIView):
    """
    API View to list and create tasks
    """
    permission_classes = [IsAuthenticated]

    def get_queryset(self) -> QuerySet[Task]:
        return Task.task.user_tasks(self.request.user).order_by('title')

    def get(self, request: Request, *args, **kwargs) -> Response:
        queryset = self.get_queryset()
        serializer = DetailedTaskSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
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

        serializer = DetailedTaskSerializer(task, data=request.data, partial=True)
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
