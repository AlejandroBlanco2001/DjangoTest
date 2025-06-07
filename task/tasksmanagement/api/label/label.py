from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from tasksmanagement.models import Label
from rest_framework.request import Request
from tasksmanagement.serializers import DetailedLabelSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import QuerySet

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
        
