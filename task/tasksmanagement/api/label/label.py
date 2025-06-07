from django.db import IntegrityError
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from tasksmanagement.models import Label
from rest_framework.request import Request
from tasksmanagement.serializers import DetailedLabelSerializer, CreateLabelSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import QuerySet
from logging import getLogger

logger = getLogger(__name__)

class LabelListCreateAPIView(ListCreateAPIView):
    """
    API View to list and create labels
    """
    permission_classes = [IsAuthenticated]
    serializer_class = DetailedLabelSerializer

    def get_queryset(self) -> QuerySet[Label]:
        return Label.label.user_labels(self.request.user).prefetch_related('tasks').sort_by('name')

    def get(self, request: Request, *args, **kwargs) -> Response:
        queryset = self.get_queryset()
        serializer = DetailedLabelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = CreateLabelSerializer(data=request.data)
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
        
