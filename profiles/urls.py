from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from profiles.views.signup import SignUp
from profiles.views.login import LogIn
from profiles.views.logout import LogOut
from profiles.views.profiles import MyProfile
from profiles.views.favourites import Favourites




urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUp.as_view(), name='sign up'),
    path('login/', LogIn.as_view(), name='log in'),
    path('logout/', LogOut.as_view(), name='log out'),
    path('myprofile/', MyProfile.as_view(), name='my profile'),
    path('myfavourites/', Favourites.as_view(), name='favorites'),

    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from .receivers import *