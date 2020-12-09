from django.views.generic import ListView

from radio.models import FavouritesList


class Favourites(ListView):
    template_name = 'profiles/favourites.html'

    def get_queryset(self):
        queryset = FavouritesList.objects.filter(user=self.request.user)
        return queryset
