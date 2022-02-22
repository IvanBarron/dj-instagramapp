from django.db import models
from django.contrib.auth.models import User

from users.models import Profile

class Post(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='posts/pictures')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
