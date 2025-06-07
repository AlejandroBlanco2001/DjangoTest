from django.urls import path
from .label import LabelListCreateAPIView

urlpatterns = [
    path('', LabelListCreateAPIView.as_view(), name='label-list-create'),
]