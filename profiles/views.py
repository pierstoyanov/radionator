from django.shortcuts import render
from django.views import View


# Create your views here.


class UserAccount(View, pk=None):

    def get(self, request):
        context = {

        }
        return render(request, 'profile.html', context)