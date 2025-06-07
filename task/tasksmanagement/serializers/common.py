from rest_framework import serializers
from tasksmanagement.models import Label, Task

class DetailedLabelSerializer(serializers.ModelSerializer):
    """ Serializer for detailed label information """
    pk = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Label
        fields = ['pk', 'name', 'owner', 'created_at', 'updated_at']
        read_only_fields = ['owner', 'created_at', 'updated_at']


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