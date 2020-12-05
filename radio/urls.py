from django.urls import path
from radio.views.radio import *
from radio.views.common import *

urlpatterns = (
    path('', RadioIndex.as_view(), name='radio index'),
    path('about/', about, name='about'),
)
