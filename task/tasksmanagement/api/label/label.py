from django.db import IntegrityError
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from tasksmanagement.api.label.permissions import CanManipulateLabel
from tasksmanagement.models import Label
from rest_framework.request import Request
from tasksmanagement.serializers import DetailedLabelSerializer, CreateLabelSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import QuerySet
from logging import getLogger
from django.shortcuts import get_object_or_404


logger = getLogger(__name__)

class LabelListCreateAPIView(ListCreateAPIView):
    """
    API View to list and create labels
    """
    permission_classes = [IsAuthenticated]
    serializer_class = DetailedLabelSerializer

    def get_queryset(self) -> QuerySet[Label]:
        return Label.label.user_labels(self.request.user).order_by('name')

    def get(self, request: Request, *args, **kwargs) -> Response:
        queryset = self.get_queryset()
        serializer = DetailedLabelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request: Request, *args, **kwargs) -> Response:
        context = {
            "request": self.request,
        }

        serializer = CreateLabelSerializer(data=request.data, context=context)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'There was an error creating the label: The name was missing'}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError as e:
            logger.error(f'Error creating label: {e}')
            return Response({'There was an error creating the label': 'Label already exists'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f'Error creating label: {e}')
            return Response({'There was an error creating the label, please try again later'}, status=status.HTTP_400_BAD_REQUEST)


class LabelDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    API View to retrieve, update and delete a label
    """
    permission_classes = [IsAuthenticated, CanManipulateLabel]
    serializer_class = DetailedLabelSerializer

    def get_object(self) -> Label:
        id = self.kwargs.get('pk')
        label = get_object_or_404(Label, id=id)
        self.check_object_permissions(self.request, label)
        return label

    def delete(self, request: Request, *args, **kwargs) -> Response:
        label = self.get_object()

        logger.info(f"Deleting label: {label.pk}")
        label.is_deleted = True
        label.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get(self, request: Request, *args, **kwargs) -> Response:
        label = self.get_object()

        serializer = DetailedLabelSerializer(label)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request: Request, *args, **kwargs) -> Response:
        label = self.get_object()

        serializer = DetailedLabelSerializer(label, data=request.data, partial=True)
        try:
            if serializer.is_valid():
                serializer.update(label, request.data)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'There was an error updating the label: The name was missing'}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError as e:
            logger.error(f'Error updating label: {e}')
            return Response({'There was an error updating the label': 'Label already exists'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f'Error updating label: {e}')
            return Response({'There was an error updating the label, please try again later'}, status=status.HTTP_400_BAD_REQUEST)
