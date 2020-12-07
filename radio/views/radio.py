from django.shortcuts import render

from django.views import View

from radio.models import RadioStation

from radio.forms.radio_form import RadioStationCreateForm

from radio.common.functionality import *
# Create your views here.


class RadioIndex(View):

    def get(self, request):

        cookie_state = test_cooke(request)
        request.session.set_test_cookie()

        context = {
            'cookie_state': cookie_state,
        }

        if RadioStation.objects.all():
            context['stations'] = RadioStation.objects.all()


        return render(request, 'home.html', context)


    def post(self, request):
        pass

