from rest_framework import serializers
from tasksmanagement.serializers import DetailedLabelSerializer
from tasksmanagement.models import Task, Label

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

class DetailedTaskLabelSerializer(DetailedTaskSerializer):
    """ Serializer for detailed task label information """
    label = DetailedLabelSerializer(many=True)

    class Meta:
        model = Task
        fields = ['pk', 'title', 'description', 'is_completed', 'owner', 'created_at', 'updated_at', 'label']
        read_only_fields = ['owner', 'created_at', 'updated_at', 'label']


class CreateTaskLabelSerializer(serializers.ModelSerializer):
    """ Serializer for connection a task with a label """
    task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all(), required=True)
    label = serializers.PrimaryKeyRelatedField(queryset=Label.objects.all(), required=True)
    
    def validate_label(self, value: Label) -> Label:
        if value.owner != self.context['request'].user:
            raise serializers.ValidationError({'label': 'You are not the owner of this label'})
        return value

    def save(self, validated_data: dict) -> Task:
        task = validated_data['task']
        label = validated_data['label']
        task.label  .add(label)
        task.save()
        return task

    class Meta:
        model = Task
        fields = ['task', 'label']
        read_only_fields = ['task', 'label']