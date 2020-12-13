from django.contrib.auth import get_user_model
from django.views.generic import ListView

from radionator.radio.models import PlayList

RadioUser = get_user_model()

from common.BackgroundMixin import BackgroundMixin


# @requires_login
class Playlists(BackgroundMixin, ListView):
    template_name = 'profiles/playlists.html'
    model = PlayList

    def get_queryset(self):
        queryset = PlayList.objects.filter(user=self.request.user)
        return queryset

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     pass