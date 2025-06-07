from django.contrib.auth.models import User
from django.db.models import QuerySet
from typing import TYPE_CHECKING
from tasksmanagement.managers.base import BaseManager

class LabelManager(BaseManager):
    """ Manager for the Label model """

    if TYPE_CHECKING:
        from tasksmanagement.models import Label
        queryset: QuerySet[Label]
    
    def user_labels(self, user: User) -> 'QuerySet[Label]':
        """Method in charge to obtain all the labels for a given user
        Args:
            user: User object
        Returns:
            QuerySet[Label]: QuerySet of Label objects
        """
        return self.filter(owner=user)
    
