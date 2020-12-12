from django.contrib import messages
from django.contrib.auth import login, get_user_model
from django.db import transaction
from django.shortcuts import render, redirect
from django.views import View

from radionator.profiles.forms import UserProfileSignupForm, SignUpForm


User = get_user_model()


class SignUp(View):
    def get(self, request):
        context = {
            'signup_form': SignUpForm(),
            'profile_form': UserProfileSignupForm(),
        }
        return render(request, 'profiles/signup.html', context)

    @transaction.atomic
    def post(self, request):
        signup_form = SignUpForm(request.POST)
        profile_form = UserProfileSignupForm(request.POST)

        if signup_form.is_valid() and profile_form.is_valid():
            user = signup_form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            login(request, user)

            # success msg and redirect to homepage
            messages.add_message(request, messages.INFO, 'Profile Created Successfully')
            return redirect('my-profile')

        else:
            # return errors from user and profiles form
            messages.add_message(request, messages.INFO, 'User creation failed:')
            messages.add_message(request, messages.INFO, f'{signup_form.errors}')
            messages.add_message(request, messages.INFO, f'{profile_form.errors}')

            # reload new forms and render the page
            context = {
                'signup_form': SignUpForm(),
                'profile_form': UserProfileSignupForm(),
            }

            return render(request, 'profiles/signup.html', context)
