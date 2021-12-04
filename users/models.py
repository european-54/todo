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
