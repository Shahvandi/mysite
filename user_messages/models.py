from django.db import models

class MessageManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(unread=True)


class Message(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    unread = models.BooleanField(default=True)
    objects = models.Manager()
    unreads = MessageManager()

    def __str__(self):
        return f'{self.name} : {self.subject} - {self.message[:30]}'
