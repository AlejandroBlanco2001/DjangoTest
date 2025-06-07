from django.urls import path
from .label import LabelListCreateAPIView, LabelDetailAPIView, TaskLabelListAPIView

urlpatterns = [
    path('', LabelListCreateAPIView.as_view(), name='label-list-create'),
    path('/<int:pk>', LabelDetailAPIView.as_view(), name='label-detail'),
    path('/<int:pk>/tasks', TaskLabelListAPIView.as_view(), name='label-task-list'),
]