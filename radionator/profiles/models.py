from django.conf import settings
from django.db import models


# Create your models here.
from radionator.radio.models import PlayList


class Profile(models.Model):
    """Profile extends the user model and stores additional information about the user."""
    BACKGROUND1 = 'bg_1'
    BACKGROUND2 = 'bg_2'
    BACKGROUND3 = 'bg_3'
    BACKGROUND4 = 'bg_4'
    BACKGROUND_CHOICES = (
        (BACKGROUND1, 'Background 1'),
        (BACKGROUND2, 'Background 2'),
        (BACKGROUND3, 'Background 3'),
        (BACKGROUND4, 'Background 4'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50, default='NoName')
    background = models.CharField(choices=BACKGROUND_CHOICES, default=BACKGROUND1, max_length=4)

    def __str__(self):
        return f'User: {self.user}, Current background: {self.background}'




# @property
# def is_faculty(self):
#     return self.groups.filter(name='Faculty group').exists()