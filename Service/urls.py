from django.urls import path, include
from .views import (
    services, service_details,
)

app_name = 'Services'

urlpatterns = [
    # Main pages

    path('services/', services, name='services'),
    path('service_details/<int:service_id>/', service_details, name='service_details'),
    

]