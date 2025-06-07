from django.urls import include, path
from tasksmanagement.api.label import urls as label_urls
from tasksmanagement.api.auth import urls as auth_urls
from tasksmanagement.api.task import urls as task_urls

urlpatterns = [
    path('label', include(label_urls)),
    path('task', include(task_urls)),
    path('auth', include(auth_urls)),
]