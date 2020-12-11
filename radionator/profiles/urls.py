from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from radionator.profiles.views.signup import SignUp
from radionator.profiles.views.login import LogIn
from radionator.profiles.views.logout import LogOut
from radionator.profiles.views.profiles import MyProfile
from radionator.profiles.views.favourites import Favourites


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUp.as_view(), name='sign up'),
    path('u-login/', LogIn.as_view(), name='log in'),
    path('u-logout/', LogOut.as_view(), name='log out'),
    path('myprofile/', MyProfile.as_view(), name='my profile'),
    path('favourites/', Favourites.as_view(), name='favorites'),


    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#import signals for creation of user related models

from .receivers import *
