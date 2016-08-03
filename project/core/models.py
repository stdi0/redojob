from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    role = models.IntegerField(default=0)

    class Meta:
        swappable = 'AUTH_USER_MODEL'

class Job(models.Model):
    name = models.CharField(max_length=150)
    employer = models.CharField(max_length=100)
    salary = models.IntegerField()
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    avatar = models.ImageField(upload_to='images/', blank=True, max_length=1000)
    phone = models.CharField(max_length=30, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name.encode('utf-8')


