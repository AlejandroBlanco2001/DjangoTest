from django.urls import path
from .label import LabelListCreateAPIView, LabelDetailAPIView

urlpatterns = [
    path('', LabelListCreateAPIView.as_view(), name='label-list-create'),
    path('/<int:pk>', LabelDetailAPIView.as_view(), name='label-detail'),
]