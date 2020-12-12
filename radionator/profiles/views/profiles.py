from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import View


# https://stackoverflow.com/questions/48040007/django-password-validation-not-working
from django.views.generic import FormView

from common.BootstrapFormMixin import BootstrapFormMixin
from radionator.profiles.forms import UserProfileSignupForm, UserProfileForm

User = get_user_model()


class MyProfile(FormView, BootstrapFormMixin):
    template_name = 'profiles/myprofile.html'
    form_class = UserProfileForm
