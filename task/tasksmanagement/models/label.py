from django.db import models
from django.contrib.auth.models import User

"""
This model should have a name and owner. Add the necessary constraints to avoid duplicate values
"""
class Label(models.Model):
    name = models.CharField(null=False, max_length=255)    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)