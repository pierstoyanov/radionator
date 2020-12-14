from django.contrib.auth import get_user_model
from django.shortcuts import render


# Create your views here.
from django.views import View

from common.BackgroundMixin import BackgroundMixin
from common.CookieTestResultMixin import test_cookie
from radionator.profiles.models import Profile

RadioUser = get_user_model()


class About(BackgroundMixin, View):
    """"Basic info about the site.
    Background and cookie mixins don't work with views.View
    Their logic needs to be added manually."""

    def get(self, request):
        request.session.set_test_cookie()

        context = {
            'cookie_state': test_cookie(request),
        }

        if self.request.user.is_authenticated:
            profile = Profile.objects.get(user=self.request.user)
            context['background'] = profile.background

        return render(request, 'about.html', context)

    def post(self, request):
        return render(request, 'about.html')

