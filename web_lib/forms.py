from django.forms import widgets
from django import forms
from .models import Book

class SearchAuthor(forms.Form):
    author_uuid = forms.UUIDField(label='Author UUID', required=False)

class PostAuthor(forms.Form):
    name = forms.CharField(max_length=200, label='Name', required=False)
    age = forms.IntegerField(label='Age', required=False)
    email = forms.EmailField(label='Email', required=False)

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            "title": "Название книги",
            "description": "Описание книги",
            "page_count": "Количество страниц",
            "author": "Выберете автора"
        }
        widgets = {"description": widgets.TextInput}
