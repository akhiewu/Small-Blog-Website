from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Contact

# Create your views here.

def deshboard(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'home.html')

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        
        values = Contact(name=name, email=email, desc=desc)
        values.save()
        
    return render(request, 'contact.html')

