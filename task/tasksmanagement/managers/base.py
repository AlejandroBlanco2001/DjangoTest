from django.db import models

class BaseManager(models.Manager):
    """
    Base manager for all models
    """
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
