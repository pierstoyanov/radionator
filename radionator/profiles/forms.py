from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from radionator.profiles.models import Profile


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'default_playlist')


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
