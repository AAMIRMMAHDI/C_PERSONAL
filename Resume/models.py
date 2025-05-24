from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


    
    

# Create your models here.
class Resume(models.Model):
    NAME = models.CharField(max_length=100, default="test")
    TITLE = models.CharField(max_length=100, default="test")
    SUBJECT = models.CharField(max_length=100, default="test")
    FIRST_TEXT = models.CharField(max_length=100, default="test")
    SECOND_TEXT = models.CharField(max_length=100, default="test")
    THIRD_TEXT = models.CharField(max_length=100, default="test")
    DESCRIPTION = models.TextField(default="test")
    scheduled = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.DESCRIPTION
    
    class Meta:
        ordering = ('created_at',)
