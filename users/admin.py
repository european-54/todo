from django.contrib import admin
from .models import Guest, Users, Notes, Frontend


admin.site.register(Users)
admin.site.register(Notes)
admin.site.register(Frontend)

