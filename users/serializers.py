from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from .models import Users, Guest, Notes, Project


class UserModelSerializer(ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'


class GuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guest
        fields = ("name", "age", "phone", "email")


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ("todo_1", "todo_2", "todo_3")


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("name", "location", "phone", "email")

