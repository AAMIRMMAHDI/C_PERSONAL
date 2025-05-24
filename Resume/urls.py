from django.urls import path, include
from .views import (
    resume,
)

app_name = 'Resume'

urlpatterns = [
    # Main pages
    path('resume/', resume, name='resume'),

]