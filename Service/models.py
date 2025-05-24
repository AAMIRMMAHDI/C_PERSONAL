from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Service(models.Model):
    name = models.CharField(max_length=100)
    scheduled = models.DateTimeField(default=timezone.now)
    content = models.TextField(default="test")
    name_servise = models.CharField(max_length=100, default="Default Service")  
    about_content = models.TextField(default="test")
    image = models.ImageField(upload_to='services', default='services/default0.jpg')
    Edelectus_content_name = models.TextField(default="test")
    Edelectus_content_Description = models.TextField(default="test")
    Temporibus_content_name = models.TextField(default="test")
    Temporibus_content_Description = models.TextField(default="test")
    Feature_content = models.TextField(default="test")
    Description_content_name = models.TextField(default="test")
    Description_content_Description = models.TextField(default="test")
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created_at',)


class ServiceComment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.service.name}'
    