from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from profiles.views.profiles import SignUp, LogIn, LogOut

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # path('acc/', UserAccount.as_view(), name='user account'),
    path('signup/', SignUp.as_view(), name='sign up'),
    path('login/', LogIn.as_view(), name='log in'),
    path('logout/', LogOut.as_view(), name='log out'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
