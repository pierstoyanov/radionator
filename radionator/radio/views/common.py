from django.shortcuts import render


# Create your views here.
from django.views import View

from common.BackgroundMixin import BackgroundMixin


class About(BackgroundMixin, View):
    def get(self, request):
        return render(request, 'about.html')

    def post(self, request):
        return render(request, 'about.html')
