from django.shortcuts import *
from .models import *

def resume(request):
    resumes = Resume.objects.filter(status=True)
    context = {
        'active_page': 'resume',
        'resumes': resumes
    }
    return render(request, "root/resume.html", context)
