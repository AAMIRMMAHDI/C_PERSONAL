from django.shortcuts import *
from .models import *

def about(request):
    abouts = About.objects.filter(status=True)
    # Always maintain a single stats record
    stats, created = Stats.objects.get_or_create(id=1)  
    context = {
        "stats": stats,
        "skills": Skill.objects.all(),  # Get all skills
        "active_page": "about",
        'abouts': abouts
    }
    return render(request, "root/about.html", context)
