from django.db import models
from django.conf import settings
from django.utils import timezone


class Message(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    message_text = models.TextField()
    message_time = models.DateTimeField(default=timezone.now())
    was_read = models.BooleanField()

    def __str__(self):
        return "Message was created by {} status: {} ".format(self.author.username, self.was_read)
