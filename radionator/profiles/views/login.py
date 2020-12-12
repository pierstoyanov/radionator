from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin

from common.BootstrapFormMixin import BootstrapFormMixin

from radionator.profiles.forms import LoginForm


User = get_user_model()


class LogIn(BootstrapFormMixin, SuccessMessageMixin, LoginView):
    template_name = 'profiles/login.html'
    form_class = LoginForm
    success_message = f'Welcome! '
