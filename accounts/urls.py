from django.urls import path
from accounts.views import *
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('profile/<int:id>/', profile, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit-profile/<int:pk>/', EditProfile.as_view(), name='edit_profile'),
   
]