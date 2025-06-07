from django.db import models
from django.contrib.auth.models import User
from label import Label
from managers import TaskManager

'''
 Task: This model should have a title, description, completion status, owner, and a many-to-many relationship to Label.
''' 
class Task(models.Model):

    task = TaskManager()

    # The combination of the title and owner should be unique
    pk = models.CompositePrimaryKey("title", "owner")
    title = models.CharField(null=False, max_length=255) 
    description = models.TextField(null=False)
    is_completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    label = models.ManyToManyField(Label, related_name='tasks')