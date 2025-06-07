from django.db import models
from typing import TYPE_CHECKING
from datetime import datetime

class SoftDeleteModel(models.Model):
    if TYPE_CHECKING:
        is_deleted: bool
        deleted_at: datetime

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True