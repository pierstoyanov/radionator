from django.contrib.auth import get_user_model
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

RadioUser = get_user_model()


class LogOut(LogoutView):
    """"Logout view, redirects to home"""
    next_page = reverse_lazy('radio index')

