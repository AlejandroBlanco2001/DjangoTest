from rest_framework import serializers
from tasksmanagement.models import Task

class DetailedTaskSerializer(serializers.ModelSerializer):
    """ Serializer for detailed label information """
    pk = serializers.CharField(read_only=True)
    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    is_completed = serializers.BooleanField(read_only=True)
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Task
        fields = ['pk', 'title', 'description', 'is_completed', 'owner', 'created_at', 'updated_at']
        read_only_fields = ['owner', 'created_at', 'updated_at']

class CreateTaskSerializer(serializers.ModelSerializer):
    """ Serializer for creating a new task """
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=True)

    class Meta:
        model = Task
        fields = ['title', 'description', 'owner']
        read_only_fields = ['owner']