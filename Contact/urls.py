from django.urls import path, include
from .views import (
    contact_view
)

app_name = 'Contact'

urlpatterns = [
    # Contact
    path('contact/', contact_view, name='contact'),
]