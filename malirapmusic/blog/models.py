from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField("Subject", max_length=255)
    content = models.TextField("Content", default="N/A")
    created_at = models.DateTimeField("Created", auto_now=True)