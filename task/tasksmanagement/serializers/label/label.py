from rest_framework import serializers
from tasksmanagement.serializers.common import DetailedLabelSerializer, DetailedTaskSerializer
from tasksmanagement.models import Label

class CreateLabelSerializer(serializers.ModelSerializer):
    """ Serializer for creating a new label """
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    name = serializers.CharField(required=True)

    class Meta:
        model = Label
        fields = ['name', 'owner']
        read_only_fields = ['owner']

class DetailedLabelTaskSerializer(DetailedLabelSerializer):
    """ Serializer for detailed task label information """
    tasks = DetailedTaskSerializer(many=True)

    class Meta:
        model = Label
        fields = ['pk', 'name', 'owner', 'created_at', 'updated_at', 'tasks']
        read_only_fields = ['owner', 'created_at', 'updated_at', 'tasks']