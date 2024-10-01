from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/default.png', null=True, blank=True)

    def __str__(self):
        return self.user.username

class Chat(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)  
    participants = models.ManyToManyField(User, related_name="chats")

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.sender}: {self.content[:50]}'