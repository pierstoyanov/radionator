from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from radionator.profiles.views.signup import SignUp
from radionator.profiles.views.login import LogIn
from radionator.profiles.views.logout import LogOut
from radionator.profiles.views.profiles import ProfileUpdate

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('signup/', SignUp.as_view(), name='sign-up'),
    path('login/', LogIn.as_view(), name='login'),
    path('logout/', LogOut.as_view(), name='logout'),

    path('myprofile/<int:pk>/', ProfileUpdate.as_view(), name='my profile'),

    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#import signals for creation of user related models

