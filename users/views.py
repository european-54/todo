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


@api_view(["GET", "POST"])
def ListView(request, api_name):
    object = pattern.get(api_name, None)
    if object == None:
        return Response(
            data="Invalid URL",
            status=status.HTTP_404_NOT_FOUND,
        )
    if request.method == "GET":
        object_list = object.model.objects.all()
        serializers = object.serializers(object_list, many=True)
        return Response(serializers.data)

    if request.method == "POST":
        data = request.data
        serializers = object.serializers(data=data)

        if not serializers.is_valid():
            return Response(
                data=serializers.error,
                status=status.HTTP_404_NOT_FOUND
            )
        serializers.save()
        return Response(
            data=serializers.error,
            status=status.HTTP_201_CREATED
        )

