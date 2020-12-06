from django.db import models
from profiles.models import UserProfile

# Create your models here.


class RadioStation(models.Model):
    POP = 'p1'
    ROCK = 'r1'
    CLASSICAL = 'c1'
    NEWS = 'n1'

    STATION_GENRES = (
        (POP, 'modern pop'),
        (ROCK, 'Rock'),
        (CLASSICAL, 'Classical'),
        (NEWS, 'News')
    )

    name = models.TextField(max_length=40)
    description = models.TextField(max_length=1000)
    genres = models.CharField(max_length=3, choices=STATION_GENRES)
    logo = models.ImageField(upload_to='logos', default='logos/default.jpg')

    def __str__(self):
        return f'Radio {self.name}, playing {" ".join(_ for _ in self.genres)}'


class FavouritesList(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    list_name = models.TextField(max_length=40, default='Playlist')
    radio_stations = models.ManyToManyField(RadioStation, default=None)


class BackgroundChoice(models.Model):
    BACKGROUND1 = 1
    BACKGROUND2 = 2
    BACKGROUND3 = 3
    BACKGROUND4 = 4
    BACKGROUND_CHOICES = (
        (BACKGROUND1, 'Background 1'),
        (BACKGROUND2, 'Background 2'),
        (BACKGROUND3, 'Background 3'),
        (BACKGROUND4, 'Background 5'),
    )

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    background = models.PositiveIntegerField(choices=BACKGROUND_CHOICES, default=1)

    def __str__(self):
        return f'User: {self.user}, Current background: {self.background}'
