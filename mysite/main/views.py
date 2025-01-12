from django.shortcuts import render
from .models import News_post


def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def services(request):
    return render(request, 'main/services.html')

def news(request):
    news = News_post.objects.all()
    return render(request, 'main/news.html', {'news': news})
