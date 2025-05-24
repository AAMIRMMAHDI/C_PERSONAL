from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import ServiceCommentForm, EditCommentForm


def services(request):
    query = request.GET.get('q')  
    services = Service.objects.filter(name__icontains=query) if query else Service.objects.all()
    context = {
        'active_page': 'services',
        'services': services
    }
    return render(request, 'root/services.html', context)

def service_details(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    comments = ServiceComment.objects.filter(service=service)
    
    if request.method == 'POST' and request.user.is_authenticated:
        if 'delete_comment' in request.POST:
            comment_id = request.POST.get('comment_id')
            comment = get_object_or_404(ServiceComment, id=comment_id, user=request.user)
            comment.delete()
            return redirect('Services:service_details', service_id=service.id)
        elif 'edit_comment' in request.POST:
            comment_id = request.POST.get('comment_id')
            comment = get_object_or_404(ServiceComment, id=comment_id, user=request.user)
            form = EditCommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('Services:service_details', service_id=service.id)
        else:
            form = ServiceCommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.service = service
                comment.user = request.user
                comment.save()
                return redirect('Services:service_details', service_id=service.id)
    else:
        form = ServiceCommentForm()
    
    return render(request, 'root/services.html', {
        'service': service,
        'comments': comments,
        'form': form,
    })