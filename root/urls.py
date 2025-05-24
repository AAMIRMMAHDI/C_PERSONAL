from django.urls import path, include
from .views import (
    home,
    signup,
    login_view, logout_view,
    password_reset_request,
    password_reset_code,
    password_change,
    change, change_profile_icon,
    save_profile_changes
)

app_name = 'root'

urlpatterns = [
    # Main pages
    path('', home, name='home'),
    
    # Authentication
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    # Password management
    path('password_reset/', password_reset_request, name='password_reset_request'),
    path('password_reset_code/', password_reset_code, name='password_reset_code'),
    path('password_change/', password_change, name='password_change'),
    
    # Profile management
    path('Change/', change, name='Change'),
    path('change-icon/', change_profile_icon, name='change_profile_icon'),
    path('save_profile_changes/', save_profile_changes, name='save_profile_changes'),
    
    # Third-party apps
    path('captcha/', include('captcha.urls')),
]