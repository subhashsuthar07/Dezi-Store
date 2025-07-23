from django.shortcuts import render, HttpResponse
from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_available=True)

    return render(request, 'home.html',{'products':products})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html') 