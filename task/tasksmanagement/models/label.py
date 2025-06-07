from django.db import models
from django.contrib.auth.models import User
from managers import LabelManager

"""
This model should have a name and owner. Add the necessary constraints to avoid duplicate values
"""
class Label(models.Model):

    label = LabelManager()

    name = models.CharField(null=False, max_length=255)    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)