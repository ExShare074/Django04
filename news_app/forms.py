from .models import News_post
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class News_postForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'text', 'date']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок новости'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите текст новости'}),
            'date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'}),
        }