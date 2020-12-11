from django.conf import settings
from django.db import models


# Create your models here.
class RadioStation(models.Model):
    """This model contains the data about a single radio station.
    It has a many to many relation with the FavouritesList model."""
    POP = 'p1'
    ROCK = 'r1'
    CLASSICAL = 'c1'
    NEWS = 'n1'

    STATION_GENRES = (
        (POP, 'Modern pop'),
        (ROCK, 'Rock'),
        (CLASSICAL, 'Classical'),
        (NEWS, 'News')
    )

    name = models.TextField(max_length=40)
    url = models.URLField()
    description = models.TextField(max_length=1000)
    genres = models.CharField(max_length=3, choices=STATION_GENRES)
    logo = models.ImageField(upload_to='logos', default='logos/default.jpg')

    def __str__(self):
        return f'Radio {self.name}, playing {" ".join(_ for _ in self.genres)}'


class FavouritesList(models.Model):
    """This is the playlist model that contains a collection of
    RadioStation instances belonging to one user.
    It has a FK relation to the User and a Many to Many relation
    with the RadioStation model. """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    list_name = models.TextField(max_length=40, default='Playlist')
    is_main = models.BooleanField(default=False)
    radio_stations = models.ManyToManyField(RadioStation, default=None)


