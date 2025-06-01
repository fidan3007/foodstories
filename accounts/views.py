from django.shortcuts import render
from accounts.models import User
from django.views.generic import CreateView
from accounts.forms import *
from django.contrib.auth.views import LoginView

class RegisterView(CreateView):
    template_name = "register.html"
    model = User
    form_class = RegisterForm
    success_url = '/'

class Login(LoginView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = '/'
    model = User

def profile(request, id):
    user = User.objects.get(id=id)
    context  = {
        'user' : user,
    }
    return render(request, 'user-profile.html', context)