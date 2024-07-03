from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from home.models import Contact

def home (request):
    return render(request, 'index.html')

def about (request):
    return render(request, 'about.html')

def education (request):
    return render(request, 'education.html')

def skills (request):
    return render(request, 'skills.html')

def experience (request):
    return render(request, 'experience.html')

def contact (request):
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fsubject=request.POST.get('subject')
        fmessage=request.POST.get('msg')
        query=Contact(name=fname, email=femail, subject=fsubject, message=fmessage)
        query.save()
        messages.success(request, "Thanks for reaching out. We'll be in touch!")
        return redirect('/contact')
    return render(request, 'contact.html')
