from django.shortcuts import render

from django.views import View

from common.CookieTestResultMixin import CookeTestResultMixin
from common.CookieTestStageMixin import CookieTestStageMixin
from radionator.radio.models import RadioStation

from radionator.radio.forms.radio_forms import RadioStationCreateForm

# Create your views here.


class RadioIndex(CookeTestResultMixin, CookieTestStageMixin, View):

    def get(self, request):
        context = {

        }
        if RadioStation.objects.all():
            context['stations'] = RadioStation.objects.all()

        return render(request, 'home.html', context)

    def post(self, request):
        pass
