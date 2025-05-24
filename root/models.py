from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/', null=True, blank=True, default='profile_pics/icon.png')
    reset_code = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return self.user.username