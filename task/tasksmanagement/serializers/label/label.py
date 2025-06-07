from rest_framework import serializers
from tasksmanagement.models import Label

class DetailedLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['id', 'name', 'tasks']