from django.shortcuts import *
from .models import *
from .forms import  *
from django.contrib import messages



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('Contact:contact')
    else:
        form = ContactForm()

    approved_contacts = Contact.objects.filter(is_approved=True)
    context = {
        'active_page': 'contact',
        'form': form,
        'approved_contacts': approved_contacts
    }
    return render(request, 'root/contact.html', context)
