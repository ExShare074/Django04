from django.contrib import admin
from django.urls import path, include
from main import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index, name='index'),
    path('news/', include('news_app.urls')),  # <<< ДОБАВЬ ЭТУ СТРОКУ
]
