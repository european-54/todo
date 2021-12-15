from datetime import timedelta
from django.db import models
from django.utils.datetime_safe import datetime


class Users(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.user = None

    username = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=128)


class Frontend(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Notes(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    frontend = models.ForeignKey(Frontend, on_delete=models.CASCADE)
    num_of_guest = models.IntegerField(default=1)
    checkin_date = models.DateField(default=datetime.now)
    checkout_date = models.DateField(default=datetime.now)
    is_checkout = models.BooleanField(default=True)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.notes = None

    def __str__(self) -> str:
        return self.guest.name

    def hotel_name(self) -> str:
        return self.user.user

    def charge(self) -> float:
        return self.is_checkout * \
               (self.checkout_date - self.checkin_date + timedelta(1)).days * \
               self.notes.price

