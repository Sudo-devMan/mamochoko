
from django.shortcuts import render
from .models import Results, FAQ

def home(r):
    results = Results.objects.all()
    return render(r, 'base.html', {"results": results})

def about(r):
    return render(r, 'about.html')

def results(r):
    results = Results.objects.all()
    return render(r, 'results.html', {"results": results})

def faq(r):
    faqs = FAQ.objects.all()
    return render(r, 'faq.html', {"faqs": faqs})

def contact(r):
    return render(r, 'contact.html')
