from django.shortcuts import render
from .models import Blog

# Create your views here.

def index(request):
    data = Blog.objects.all().order_by('-id')
    return render(request, "index.html", {'data':data})
