from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View

from common.BootstrapFormMixin import BootstrapFormMixin
from profiles.forms import LoginForm
#
# def get_redirect_url(params):
#     redirect_url = params.get('return_url')
#     return redirect_url if redirect_url else 'index'
#


class LogIn(LoginView, BootstrapFormMixin):
    # form_class = LoginForm
    template_name = 'profiles/login.html'


# class LogIn(View):
#     def get(self, request):
#         context = {
#             'login_form': LoginForm()
#         }
#         return render(request, 'profiles/login.html', context)
#
#     def post(self, request):
#         login_form = LoginForm(request.POST)
#
#         if login_form.is_valid():
#             username = login_form.cleaned_data['username']
#             password = login_form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#
#             return_url = get_redirect_url(request.POST)
#
#             if user:
#                 login(request, user)
#                 return redirect(return_url)
#         return render(request, 'profiles/login.html')

