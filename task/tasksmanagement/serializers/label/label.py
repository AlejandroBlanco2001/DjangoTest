from rest_framework import serializers
from tasksmanagement.models import Label
from django.contrib.auth.models import User

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

class CreateLabelSerializer(serializers.ModelSerializer):
    """ Serializer for creating a new label """
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    name = serializers.CharField(required=True)

    class Meta:
        model = Label
        fields = ['name', 'owner']
        read_only_fields = ['owner']