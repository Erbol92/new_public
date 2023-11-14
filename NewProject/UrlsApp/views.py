from django.shortcuts import render, redirect
from .models import Urls

# Create your views here.

def home(request):
    
    ctx = {
        'title':'Main',
    }
    return render(request,'UrlsApp/home.html',ctx)