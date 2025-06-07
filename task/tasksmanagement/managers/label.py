from django.db import models
from django.contrib.auth.models import User
from django.db.models import QuerySet
from ..models import Label

class LabelManager(models.Manager):
    """ Manager for the Label model """
    
    def user_labels(self, user: User) -> QuerySet[Label]:
        """Method in charge to obtain all the labels for a given user
        Args:
            user: User object
        Returns:
            QuerySet[Label]: QuerySet of Label objects
        """
        return self.filter(owner=user)
    
