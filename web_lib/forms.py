
from django import forms

class SearchAuthor(forms.Form):
    author_uuid = forms.UUIDField(label='Author UUID', required=False)

class PostAuthor(forms.Form):
    name = forms.CharField(max_length=200, label='Name', required=False)
    age = forms.IntegerField(label='Age', required=False)
    email = forms.EmailField(label='Email', required=False)