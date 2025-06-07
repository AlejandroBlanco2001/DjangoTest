from rest_framework import serializers
from tasksmanagement.models import Task, Label
from tasksmanagement.serializers.common import DetailedTaskSerializer, DetailedLabelSerializer

class CreateTaskSerializer(serializers.ModelSerializer):
    """ Serializer for creating a new task """
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    is_completed = serializers.BooleanField(required=False)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.is_completed = validated_data.get('is_completed', instance.is_completed)
        instance.save(update_fields=['title', 'description', 'is_completed'])
        return instance

    class Meta:
        model = Task
        fields = ['title', 'description', 'owner', 'is_completed']
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

        if task.label.filter(id=label.id).exists():
            raise serializers.ValidationError({'label': 'This label is already associated with this task'})

        task.label.add(label)
        task.save()
        return task

    class Meta:
        model = Task
        fields = ['task', 'label']
        read_only_fields = ['task', 'label']