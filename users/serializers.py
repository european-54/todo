from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from .models import Users, Guest, Notes, Project


class UserModelSerializer(ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'
