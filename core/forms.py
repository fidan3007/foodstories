from django import forms
from core.models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Your Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Your Email'}),
            'subject': forms.TextInput(attrs={'class':'form-control','placeholder':'Subject'}),
            'message': forms.Textarea(attrs={'class':'form-control','placeholder':'Message'}),
        }

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'desription', 'text', 'image', 'category', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'title'}),
            'desription': forms.TextInput(attrs={'class':'form-control','placeholder':'desription'}),
            'text': forms.TextInput(attrs={'class':'form-control','placeholder':'text'}),
            'images': forms.FileInput(attrs={'class':'form-control','placeholder':'image'}),
            'category': forms.Select(attrs={'class':'form-control','placeholder':'category'}),
            'tags': forms.SelectMultiple(attrs={'class':'form-control','placeholder':'tags'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]
        widgets = {
            'text': forms.Textarea(attrs={'class':'form-control','placeholder':'Comment'}),
        }