from django.contrib import messages
from django.contrib.auth import user_logged_out, get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from radionator.radio.models import PlayList

RadioUser = get_user_model()


@receiver(post_save, sender=RadioUser)
def user_created(sender, instance, created, *args, **kwargs):
    """This signal track the creation of new users and
    adds a PlayList in DB for the user."""
    if created:
        play_list = PlayList(
            user=instance,
            list_name='My First Station List',
            is_user_default=True)
        play_list.save()


@receiver(user_logged_out, sender=RadioUser)
def logout_message(sender, user, request, **kwargs):
    """Display USERNAME logged out message."""
    messages.add_message(request, messages.INFO,
                         f'{user.username} logged out Successfully')
