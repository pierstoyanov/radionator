from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from common.BackgroundMixin import BackgroundMixin
from common.BootstrapFormMixin import BootstrapFormMixin
from common.CookieTestResultMixin import CookeTestResultMixin
from common.CookieTestStageMixin import CookieTestStageMixin

from radionator.profiles.forms import LoginForm


RadioUser = get_user_model()


class LogIn(BootstrapFormMixin,
            SuccessMessageMixin,
            BackgroundMixin,
            CookeTestResultMixin,
            CookieTestStageMixin,
            LoginView):
    """Generic view for user login."""
    template_name = 'profiles/login.html'
    form_class = LoginForm

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO,
                             f'Welcome back!')
        return reverse_lazy('radio index')
