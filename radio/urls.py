from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from radio.views.radio import *
from radio.views.common import *

urlpatterns = [
                  path('', RadioIndex.as_view(), name='radio index'),
                  path('about/', about, name='about'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
