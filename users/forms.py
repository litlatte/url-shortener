from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    username = forms.SlugField(max_length=30, required=True, help_text="Required")
    email = forms.EmailField(max_length=254, required=True, help_text="Required")
    

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            ]