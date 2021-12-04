from django.contrib import admin
from django.contrib import admin
from .models import Guest, Notes, Users, Project
admin.site.register(Users)
admin.site.register(Guest)
admin.site.register(Notes)
admin.site.register(Project)

