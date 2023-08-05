from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return str(self.name)

# Room will be a child of a topic
# A topic can have multiple rooms but a room can have a single topic
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) #ONE-TO-MANY RELATIONSHIP
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) #ONE-TO-MANY RELATIONSHIP
    name = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True) #null=True tells that this field can't be null or empty
    #participant = 
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return str(self.name)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #ONE-TO-MANY RELATIONSHIP
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #ONE-TO-MANY RELATIONSHIP
    body = models.TextField()
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.body[0:50])    

    

