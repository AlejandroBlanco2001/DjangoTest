from django.db import models
from django.contrib.auth.models import User
from django.db.models import QuerySet
from typing import TYPE_CHECKING
from tasksmanagement.managers.base import BaseManager

class TaskManager(BaseManager):
    """ Manager for the Task model """

    if TYPE_CHECKING:
        from tasksmanagement.models import Task
        queryset: QuerySet[Task]
    
    def user_tasks(self, user: User) -> 'QuerySet[Task]':
        """Method in charge to obtain all the tasks for a given user
        Args:
            user: User object
        Returns:
            QuerySet[Task]: QuerySet of Task objects
        """
        return self.filter(owner=user)
    
