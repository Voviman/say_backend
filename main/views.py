from django.shortcuts import render
from .models import Blog, Driver

# Create your views here.

def index(request):
    if request.method == 'POST':
        form_data = request.POST


        driver = Driver.objects.create(
            name = form_data['name'],
            email = form_data['email'],
            number = form_data['number'],
            exp = form_data['exp'],
            text = form_data['text'],
        )

        driver.save()
        data = Blog.objects.all().order_by('-id')
        return render(request, "index.html", {'data':data})

        

    else:
        data = Blog.objects.all().order_by('-id')
        return render(request, "index.html", {'data':data})

