from django.shortcuts import render

from django.views import View

from common.CookieTestResultMixin import CookeTestResultMixin
from common.CookieTestStageMixin import CookeTestStageMixin
from radionator.radio.models import RadioStation

from radionator.radio.forms.radio_form import RadioStationCreateForm

# Create your views here.


class RadioIndex(View, CookeTestStageMixin, CookeTestResultMixin):

    def get(self, request):
        context = {

        }
        if RadioStation.objects.all():
            context['stations'] = RadioStation.objects.all()

        return render(request, 'home.html', context)

    def post(self, request):
        pass
