from django.shortcuts import render
from accounts.models import User
from django.views.generic import CreateView


class RegisterView(CreateView):
    template_name = "register.html"
    model = User
