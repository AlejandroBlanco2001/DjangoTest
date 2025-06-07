from rest_framework import serializers
from tasksmanagement.models import Label

class DetailedLabelSerializer(serializers.ModelSerializer):
    """ Serializer for detailed label information """
    class Meta:
        model = Label
        fields = ['id', 'name', 'tasks']

class CreateLabelSerializer(serializers.ModelSerializer):
    """ Serializer for creating a new label """
    class Meta:
        model = Label
        fields = ['name']