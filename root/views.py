from django.shortcuts import *
from .models import *
from .forms import  *
from django.contrib.auth.decorators import *
from django.contrib.auth import *
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.contrib.auth.models import *
from django.contrib import messages
import random

def home(request):
    context = {
        'active_page': 'home'
    }
    return render(request, "root/index.html", context)



@login_required
def change_profile_icon(request):
    user_profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = ProfileIconForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile icon has been updated.")
            return redirect('root:Change')
    else:
        form = ProfileIconForm(instance=user_profile)

    context = {
        'active_page': 'change',
        'form': form
    }
    return render(request, 'new_Page/change_icon.html', context)

@login_required
def change(request):
    context = {
        'active_page': 'change'
    }
    return render(request, "new_Page/Change.html", context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('root:home')
    else:
        form = SignUpForm()

    context = {
        'active_page': 'signup',
        'form': form
    }
    return render(request, 'account/signup.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                messages.success(request, 'Logged in successfully.')
                return redirect('root:home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    context = {
        'active_page': 'login',
        'form': form
    }
    return render(request, 'account/login.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('root:home')

def generate_reset_code():
    return str(random.randint(1000, 9999))

def password_reset_request(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            reset_code = generate_reset_code()
            user_profile, _ = UserProfile.objects.get_or_create(user=user)
            user_profile.reset_code = reset_code
            user_profile.save()
            print(f"Reset code: {reset_code}")  # In production, send via email
            return redirect('root:password_reset_code')
        except User.DoesNotExist:
            messages.error(request, 'No user found with this email.')

    context = {
        'active_page': 'password_reset_request'
    }
    return render(request, 'account/password_reset_request.html', context)

def password_reset_code(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            user_profile = UserProfile.objects.get(reset_code=code)
            request.session['user_id'] = user_profile.user.id
            return redirect('root:password_change')
        except UserProfile.DoesNotExist:
            messages.error(request, 'Invalid reset code.')

    context = {
        'active_page': 'password_reset_code'
    }
    return render(request, 'account/password_reset_code.html', context)

def password_change(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = get_object_or_404(User, id=user_id)
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password changed successfully. Please login again.')
                return redirect('root:login')
        else:
            form = SetPasswordForm(user)

        context = {
            'active_page': 'password_change',
            'form': form
        }
        return render(request, 'account/password_change.html', context)

    messages.error(request, 'Please enter your reset code first.')
    return redirect('root:password_reset_request')

@login_required
def save_profile_changes(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username', user.username)
        user.email = request.POST.get('email', user.email)
        user.first_name = request.POST.get('first_name', user.first_name)
        user.save()
        messages.success(request, 'Changes saved successfully.')
        return redirect('root:home')

    return redirect('root:change')