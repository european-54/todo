from django.db import models
from rest_framework import serializers


class Users(models.Model):
    username = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=128)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.name = None

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    mame = models.CharField(max_length=64)
    link_in_repo = models.CharField(max_length=256)


class Guest(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name
