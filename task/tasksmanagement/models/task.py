from django.db import models
from django.contrib.auth.models import User
from tasksmanagement.managers import TaskManager
from typing import TYPE_CHECKING
from django.db.models import QuerySet
from django.db.models import UniqueConstraint
from tasksmanagement.models.timestamp import TimeStampedModel
from tasksmanagement.models.soft_delete import SoftDeleteModel

'''
 This model should have a title, description, completion status, owner, and a many-to-many relationship to Label.
''' 
class Task(TimeStampedModel, SoftDeleteModel):

    if TYPE_CHECKING:
        queryset: QuerySet['Task']
        title: str
        description: str
        is_completed: bool
        owner: User

    objects = TaskManager()

    title = models.CharField(null=False, max_length=255) 
    description = models.TextField(null=False)
    is_completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    label = models.ManyToManyField(
        "Label", 
        related_name='tasks'
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['title', 'owner_id'],
                name='unique_title_owner'
            )
        ]