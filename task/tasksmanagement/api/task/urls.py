from django.urls import path
from .task import TaskListCreateAPIView, TaskDetailAPIView, TaskLabelListCreateAPIView

urlpatterns = [
    path('', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('/<int:pk>', TaskDetailAPIView.as_view(), name='task-detail'),
    path('/<int:pk>/labels', TaskLabelListCreateAPIView.as_view(), name='task-label-list-create'),
]