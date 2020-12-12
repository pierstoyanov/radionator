from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View


# https://stackoverflow.com/questions/48040007/django-password-validation-not-working
from django.views.generic import FormView, DetailView, UpdateView

from common.BackgroundMixin import BackgroundMixin
from common.BootstrapFormMixin import BootstrapFormMixin
from radionator.profiles.forms import UserProfileSignupForm, UserProfileViewForm
from radionator.profiles.models import Profile

User = get_user_model()


class ProfileUpdate(BackgroundMixin, BootstrapFormMixin, UpdateView):
    model = Profile
    fields = ('background',)
    template_name_suffix = '_update_form'
    # form_class = UserProfileViewForm
    success_url = reverse_lazy('my profile')

    def get_object(self):
        return Profile.objects.get(user=self.request.user.pk)
