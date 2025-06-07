from django.db import models
from typing import TYPE_CHECKING
from datetime import datetime

class TimeStampedModel(models.Model):
    if TYPE_CHECKING:
        created_at: datetime
        updated_at: datetime

    """Abstract base class that adds created_at and updated_at fields to models."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True