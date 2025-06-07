from django.urls import include, path
from tasksmanagement.api.label import urls as label_urls

urlpatterns = [
    path('labels/', include(label_urls)),
]