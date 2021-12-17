from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Post, User

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email')


class postCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body']