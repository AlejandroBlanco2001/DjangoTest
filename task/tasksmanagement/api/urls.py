from django.urls import include, path
from tasksmanagement.api.label import urls as label_urls
from tasksmanagement.api.auth import urls as auth_urls

urlpatterns = [
    path('labels/', include(label_urls)),
    path('auth/', include(auth_urls)),
]