from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=128)


class Guest(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

