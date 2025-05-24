from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from captcha.fields import CaptchaField




class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    captcha = CaptchaField() 
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
        }



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    captcha = CaptchaField()





class CustomPasswordResetForm(PasswordResetForm):
    def send_mail(self, subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name=None, request=None):
        print(f"Subject: {self.get_subject(subject_template_name, context)}")
        print(f"Email to: {to_email}")
        print(f"Message: {self.get_email_body(email_template_name, context)}")




from django import forms
from .models import UserProfile

class ProfileIconForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']

from django import forms

