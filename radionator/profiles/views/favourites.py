from django.contrib.auth import get_user_model
from django.views.generic import ListView

from radionator.radio.models import PlayList

User = get_user_model()

# @requires_login
class Favourites(ListView):
    template_name = 'profiles/favourites.html'
    model = PlayList

    def get_queryset(self):
        queryset = PlayList.objects.filter(user=self.request.user)
        return queryset

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     pass