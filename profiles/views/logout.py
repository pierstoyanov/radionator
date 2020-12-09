from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


class LogOut(LogoutView):
    next_page = reverse_lazy('radio index')

    def logout_message(self):
        messages.add_message(self.request, messages.INFO,
                             f'{self.request.user.name} logged out Successfully')
        return super()