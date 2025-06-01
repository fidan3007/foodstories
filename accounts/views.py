from django.shortcuts import render
from accounts.models import User
from django.views.generic import CreateView
from accounts.forms import *

class RegisterView(CreateView):
    template_name = "register.html"
    model = User
    form_class = RegisterForm
    succes_url = 'accounts/login'
