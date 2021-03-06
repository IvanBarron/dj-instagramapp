from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """Profile Model

    Proxy model that extend from User 
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20)
    picture = models.ImageField(
        upload_to='users/photo',
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username