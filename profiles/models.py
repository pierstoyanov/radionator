from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    BACKGROUND1 = 'bg_1'
    BACKGROUND2 = 'bg_2'
    BACKGROUND3 = 'bg_3'
    BACKGROUND4 = 'bg_4'
    BACKGROUND_CHOICES = (
        (BACKGROUND1, 'Background 1'),
        (BACKGROUND2, 'Background 2'),
        (BACKGROUND3, 'Background 3'),
        (BACKGROUND4, 'Background 5'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    background = models.PositiveIntegerField(choices=BACKGROUND_CHOICES, default=1)

    def __str__(self):
        return f'User: {self.user}, Current background: {self.background}'
