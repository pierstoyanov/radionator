from django.contrib.auth.models import User
from django.db import models
from radionator.profiles.models import Profile

# Create your models here.


class RadioStation(models.Model):
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    list_name = models.TextField(max_length=40, default='Playlist')
    is_main = models.BooleanField(default=False)
    radio_stations = models.ManyToManyField(RadioStation, default=None)


