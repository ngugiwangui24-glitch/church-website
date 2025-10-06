from django.db import models
from django.contrib.auth.models import User  # For associating events/sermons with users

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Sermon(models.Model):
    title = models.CharField(max_length=200)
    preacher = models.CharField(max_length=100)
    content = models.TextField()  # Can expand to FileField for audio/video later
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title