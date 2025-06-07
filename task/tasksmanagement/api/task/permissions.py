from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import View
from tasksmanagement.models import Task

class CanManipulateTask(BasePermission):
    """
    Permission to check if the user can manipulate the label
    """
    def has_object_permission(self, request: Request, view: View, obj: Task) -> bool:
        return obj.owner == request.user