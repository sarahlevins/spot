from django.db import models
from users.models import CustomUser


class Message(models.Model):
    time = models.DateTimeField()
    sender = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='sender')
    reciever = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='reciever')
    content = models.TextField()
