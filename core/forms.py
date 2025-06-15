from django import forms
from core.models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Your Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Your Emai;'}),
            'subject': forms.TextInput(attrs={'class':'form-control','placeholder':'Subject'}),
            'message': forms.Textarea(attrs={'class':'form-control','placeholder':'Message'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]
        widgets = {
            'text': forms.Textarea(attrs={'class':'form-control','placeholder':'Comment'}),
        }