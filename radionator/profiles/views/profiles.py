from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import View


# https://stackoverflow.com/questions/48040007/django-password-validation-not-working
from django.views.generic import FormView

from radionator.profiles.forms import UserProfileForm

User = get_user_model()

class LogOut(View):
    def get(self, request):
        context = {

        }
        return render(request, 'profiles/logout.html', context)

    def post(self, request):
        context = {

        }
        return render(request, 'profiles/logout.html', context)


class MyProfile(FormView):
    template_name = 'profiles/myprofile.html'
    form_class = UserProfileForm
