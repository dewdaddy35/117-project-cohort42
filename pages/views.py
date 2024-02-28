from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def home(request):
    return render(request, 'pages/about_me.html')


def project(request):
    return render(request, 'pages/project.html')

def experience(request):
    return render(request, 'pages/experience.html')

def contact_view(request):
    form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})


