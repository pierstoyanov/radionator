from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from profiles.forms.forms import SignUpForm, UserProfileForm

# https://stackoverflow.com/questions/48040007/django-password-validation-not-working


class SignUp(View):
    def get(self, request):
        context = {
            'signup_form': SignUpForm(),
            'profile_form': UserProfileForm(),
        }
        return render(request, 'profile/signup.html', context)

    def post(self, request):
        signup_form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if signup_form.is_valid():
            user = signup_form.save()
            profile = profile_form.save()

            profile.user = user
            profile.save()

            # user = form.save(commit=False)
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            #
            # try:
            #     validate_password(password, user)
            #
            # except ValidationError as e:
            #     form.add_error('password', e)
            #     return render(request, 'profile/signup.html', {'form': form})

            login(request, user)
            messages.add_message(request, messages.INFO, 'Profile Created')
            return redirect('radio index')
        else:
            context = {
                'signup_form': SignUpForm(),
                'profile_form': UserProfileForm(),
            }
            messages.add_message(request, messages.INFO, 'User creation failed')
            return render(request, 'profile/signup.html', context)


class LogIn(View):
    def get(self, request):
        context = {

        }
        return render(request, 'profile/login.html', context)

    def post(self, request):
        context = {

        }
        return render(request, 'profile/login.html', context)


class LogOut(View):
    def get(self, request):
        context = {

        }
        return render(request, 'profile/logout.html', context)

    def post(self, request):
        context = {

        }
        return render(request, 'profile/logout.html', context)


class UserAccount(View):
    def get(self, request):
        context = {

        }
        return render(request, 'profile/myprofile.html', context)

    def post(self, request):
        pass
