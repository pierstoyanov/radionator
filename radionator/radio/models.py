from django.conf import settings
from django.db import models


# Create your models here.
from django.utils.text import slugify


class RadioStation(models.Model):
    """This model contains the data about a single radio station.
    It has a many to many relation with the PlayList model."""

    POP = 'p1'
    ROCK = 'r1'
    CLASSICAL = 'c1'
    NEWS = 'n1'

    STATION_GENRES = (
        (POP, 'Pop'),
        (ROCK, 'Rock'),
        (CLASSICAL, 'Classical'),
        (NEWS, 'News')
    )

    name = models.TextField(max_length=40)
    slug = models.SlugField(editable=False,)
    url = models.URLField()
    description = models.TextField(max_length=1000)
    genres = models.CharField(max_length=3, choices=STATION_GENRES)
    logo = models.ImageField(upload_to='logos', default='logos/default.jpg')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'Radio {self.name}, playing {" ".join(_ for _ in self.genres)}'


class PlayList(models.Model):
    """This is the playlist model that contains a collection of
    RadioStation instances belonging to one user.
    It has a ForeignKey relation to the User and a Many to Many relation
    with the RadioStation model. """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(editable=False, )
    list_name = models.TextField(max_length=40, default='Playlist')
    is_user_default = models.BooleanField(default=False)
    radio_stations = models.ManyToManyField(RadioStation, default=None)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.list_name)
        return super().save(*args, **kwargs)
