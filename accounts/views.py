from django.shortcuts import render
from accounts.models import User
from django.views.generic import CreateView, UpdateView
from accounts.forms import *
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy

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

class EditProfile(UpdateView):
    template_name = "register.html"
    model = User
    form_class = EditProfileForm
    
    def get_success_url(self):
        return reverse_lazy('accounts:profile', args=[self.request.user.id])

class ForgetPassword(PasswordResetView):
    template_name= "forget_password.html"
    success_url = reverse_lazy('accounts:login')
    form_class = ForgetPasswordForm
    email_template_name = "forget-password-email.html"
