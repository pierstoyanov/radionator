from django.contrib.auth import get_user_model
from django.shortcuts import render

from django.views import View

from common.BackgroundMixin import BackgroundMixin
from common.CookieTestResultMixin import CookeTestResultMixin, test_cookie
from common.CookieTestStageMixin import CookieTestStageMixin
from radionator.profiles.models import Profile
from radionator.radio.models import RadioStation

from radionator.radio.forms.radio_forms import RadioStationCreateForm

# Create your views here.
RadioUser = get_user_model()


class RadioIndex(View):
    """"This the base view of the app.
    Background and cookie mixins don't work with views.View.
    Their logic needs to be added manually."""
    def get(self, request):
        request.session.set_test_cookie()

        context = {
            'cookie_state': test_cookie(request),
        }

        if self.request.user.is_authenticated:
            profile = Profile.objects.get(user=self.request.user)
            context['background'] = profile.background

        if RadioStation.objects.all():
            context['stations'] = RadioStation.objects.all()

        return render(request, 'home.html', context)

    def post(self, request):
        return render(request, 'home.html')
