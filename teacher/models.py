from django.contrib.auth.models import User
from django.db import models


class Teacher(User):
    image = models.ImageField(upload_to='teachers/')
