from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm


def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., send an email)
            messages.success(request, 'Thank you for your message. We will get back to you shortly.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})

def terms_of_service(request):
    return render(request, 'core/terms_of_service.html')

def privacy_policy(request):
    return render(request, 'core/privacy_policy.html')
