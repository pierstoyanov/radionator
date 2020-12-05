from django.shortcuts import render

from django.views import View

# Create your views here.


class RadioIndex(View):

    def get(self, request):
        context = {

        }
        return render(request, 'radio.html', context)

    def post(self, request):
        pass

