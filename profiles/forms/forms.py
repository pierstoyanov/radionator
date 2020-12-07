from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from profiles.models import UserProfile


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email',)
        widgets = {
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']

    # def __init__(self, *args, **kwargs):
    #     super(UserProfileForm, self).__init__(*args, **kwargs)
    #
    #     self.widgets = {
    #         'background': forms.TextInput(attrs={
    #             'title': 'Choose your background. This can be changed later.',
    #             'class': 'background-choice',
    #             }
    #         )
    #     }
