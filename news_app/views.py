from django.shortcuts import render, redirect
from .forms import News_postForm
from .models import News_post

def home(request):
    news = News_post.objects.all()
    return render(request, 'news_app/news.html', {'news': news})

def create_news(request):
    error = ''
    if request.method == 'POST':
        form = News_postForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "данные не валидны"
    form = News_postForm()
    return render(request, 'news_app/add_new_post.html', {'form': form}, {'error': error})