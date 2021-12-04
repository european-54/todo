from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Users, Guest, Project, Notes
from .serializers import UserModelSerializer, GuestSerializer, NotesSerializer, ProjectSerializer

from collections import namedtuple


class UserModelViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserModelSerializer


nt = namedtuple("object", ["model", "serializers"])
pattern = {
    "guest": nt(Guest, GuestSerializer),
    "notes": nt(Notes, NotesSerializer),
    "project": nt(Project, ProjectSerializer),
    "users": nt(Users, UserModelSerializer),
    }

