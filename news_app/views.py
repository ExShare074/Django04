from django.shortcuts import render
from .models import News_post

def home(request):
    news = News_post.objects.all()
    return render(request, 'news_app/news.html', {'news': news})

def create_news(request):
        return render(request, 'news_app/add_new_post.html')