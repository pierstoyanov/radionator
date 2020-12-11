from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


class LogOut(LogoutView):
    next_page = reverse_lazy('radio index')

