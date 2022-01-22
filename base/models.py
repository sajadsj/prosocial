from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)  #null = treu means it could not be empty blank is for form method
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True) #every single time save 
    created = models.DateTimeField(auto_now_add=True) #first save or crate 

    class Meta:
        ordering = ['-updated', '-created']


    def __str__(self):
        return self.name




class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) #every single time save 
    created = models.DateTimeField(auto_now_add=True) #first save or crate 
    
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]  #shwo only first 50 char of msg