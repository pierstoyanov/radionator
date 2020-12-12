from django.shortcuts import render

from django.views import View

from common.BackgroundMixin import BackgroundMixin
from common.CookieTestResultMixin import CookeTestResultMixin
from common.CookieTestStageMixin import CookieTestStageMixin
from radionator.profiles.models import Profile
from radionator.radio.models import RadioStation

from radionator.radio.forms.radio_forms import RadioStationCreateForm

# Create your views here.


class RadioIndex(View):
    """"This the base view of the app.
    Background and cookie mixins don't work with views.View"""
    def get(self, request):

        context = {

        }

        if self.request.user.is_authenticated:
            profile = Profile.objects.get(user=self.request.user)
            context['background'] = profile.background

        if RadioStation.objects.all():
            context['stations'] = RadioStation.objects.all()

        return render(request, 'home.html', context)

    def post(self, request):
        pass
