from django.urls import path, include
from .views import (
    about,

)

app_name = 'About'

urlpatterns = [
    # Main pages
    path('about/', about, name='about'),

]