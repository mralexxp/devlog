from django.db import models
from django.utils import timezone


class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='')

    def __str__(self):
        return self.title


class Records(models.Model):
    title = models.CharField(max_length=200)
    version = models.CharField(max_length=20)
    prefix = models.CharField(max_length=20, default='')
    changelog = models.TextField(default='')
    documentation = models.TextField(default='')
    pubdate = models.DateTimeField(timezone.now)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
