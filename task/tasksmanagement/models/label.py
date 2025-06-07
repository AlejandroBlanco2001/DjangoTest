from django.db import models
from django.contrib.auth.models import User
from tasksmanagement.managers import LabelManager
from typing import TYPE_CHECKING
from django.db.models import QuerySet
from django.db.models import UniqueConstraint
from tasksmanagement.models.timestamp import TimeStampedModel
from tasksmanagement.models.soft_delete import SoftDeleteModel

"""
This model should have a name and owner. Add the necessary constraints to avoid duplicate values
"""
class Label(TimeStampedModel, SoftDeleteModel):
    if TYPE_CHECKING:
        queryset: QuerySet['Label']
        name: str
        owner: User

    label = LabelManager()

    name = models.CharField(null=False, max_length=255)    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['name', 'owner_id'],
                name='unique_name_owner'
            )
        ]