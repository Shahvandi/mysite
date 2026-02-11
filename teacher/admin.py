from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .models import Teacher, Otp

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Teacher)
admin.site.register(Otp)