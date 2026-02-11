from django.contrib.auth.models import User
from django.db import models


class Teacher(User):
    image = models.ImageField(upload_to='teachers/')

class Otp(models.Model):
    email = models.CharField(max_length=11)
    token = models.CharField(max_length=100,unique=True, null=True)
    code = models.SmallIntegerField()