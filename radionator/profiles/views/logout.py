from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

User = get_user_model()


class LogOut(LogoutView):
    next_page = reverse_lazy('radio index')

