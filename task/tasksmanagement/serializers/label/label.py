from rest_framework import serializers
from tasksmanagement.models import Label
from django.contrib.auth.models import User

class DetailedLabelSerializer(serializers.ModelSerializer):
    """ Serializer for detailed label information """
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    owner_username = serializers.SerializerMethodField(read_only=True)
    owner_id = serializers.SerializerMethodField(read_only=True)

    def get_owner_username(self, obj: Label) -> str:
        return obj.owner.username
    
    def get_owner_id(self, obj: Label) -> int:
        return obj.owner.id

    class Meta:
        model = Label
        fields = ['pk', 'name', 'owner_username', 'owner_id']
        read_only_fields = ['owner_username', 'owner_id']

class CreateLabelSerializer(serializers.ModelSerializer):
    """ Serializer for creating a new label """
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    name = serializers.CharField(required=True)

    class Meta:
        model = Label
        fields = ['name', 'owner']
        read_only_fields = ['owner']