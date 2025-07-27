from django import forms
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordResetForm, SetPasswordForm




class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2', 'image', 'info', ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'image': forms.FileInput(attrs={'class':'form-control','placeholder':'Image'}),
            'info' : forms.Textarea(attrs={'class':'form-control','placeholder':'Info'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
        }


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User 
        fields = ['first_name', 'last_name','username', 'email', 'image', 'info',]
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'image': forms.FileInput(attrs={'class':'form-control','placeholder':'Image'}),
            'info' : forms.Textarea(attrs={'class':'form-control','placeholder':'Info'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
        }


class ForgotPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))

    class Meta:
        model = User
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
        }

class ForgotPasswordConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'New Password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm New Password'}))
    class Meta:
        model = User
        fields = ['new-password1', 'new_password2']



