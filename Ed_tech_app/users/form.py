from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile 


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    profile_image = forms.ImageField(default = 'default.jpg', upload_to='profile_pics')
    class Meta():
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2', 'profile_image']
