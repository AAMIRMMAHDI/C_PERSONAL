from django.db import models
from django.utils import timezone




class About(models.Model):
    PAGE_NAME = models.CharField(max_length=100, default="test")
    A_LITTLE_ABOUT_US = models.CharField(max_length=100, default="test")
    CREATOR_NAME = models.CharField(max_length=100, default="test")
    ROLE = models.CharField(max_length=100, default="test")
    EMAIL = models.CharField(max_length=100, default="test")
    SERVICES = models.CharField(max_length=100, default="test")
    INTERESTS = models.CharField(max_length=100, default="test")
    ONLINE_PRESENTATION = models.CharField(max_length=100, default="test")
    WORK_HISTORY = models.CharField(max_length=100, default="test")
    DESCRIPTION = models.TextField(default="test")
    scheduled = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.PAGE_NAME
    
    class Meta:
        ordering = ('created_at',)



from django.db import models

class Stats(models.Model):
    happy_clients = models.IntegerField(default=0)
    projects = models.IntegerField(default=0)
    hours_of_support = models.IntegerField(default=0)
    hard_workers = models.IntegerField(default=0)

    def __str__(self):
        return "Statistics"



class Skill(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    percentage = models.IntegerField(verbose_name="درصد", help_text="عدد بین 0 تا 100")

    def __str__(self):
        return f"{self.title} - {self.percentage}%"