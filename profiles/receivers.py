from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


from radio.models import FavouritesList


@receiver(post_save, sender=User)
def user_created(sender, instance, created, *args, **kwargs):
    if created:
        favourites_list = FavouritesList(user=instance,
                                         list_name='My First Station List')
        favourites_list.save()



