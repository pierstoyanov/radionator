from django.db import models

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

    name = models.TextField(max_length=50)
    genres = models.CharField(max_length=3, choices=STATION_GENRES)

    def __str__(self):
        return f'Radio {self.name}, playing {" ".join(_ for _ in self.genres)}'


class FavouritesList(models.Model):
    pass