from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from radionator.radio.views.home import RadioIndex
from radionator.radio.views.common import About
from radionator.radio.views.playlist_crud import \
        CreatePlayList, PlayListDetails, EditPlayList, DeletePlayList
from radionator.radio.views.radio_crud import \
        AddRadio, RadioDetails, EditRadio, DeleteRadio


urlpatterns = [
        path('', RadioIndex.as_view(), name='radio index'),
        path('about/', About.as_view(), name='about'),

        path('add/', AddRadio.as_view(), name='add radio'),
        path('<int:pk>/<slug:slug>/', RadioDetails.as_view(), name='radio details'),
        path('edit/<int:pk>/<slug:slug>', EditRadio.as_view(), name='edit radio'),
        path('delete/<int:pk>/<slug:slug>/', DeleteRadio.as_view(), name='delete radio'),

        path('playlist/add/', CreatePlayList.as_view(), name='create playlist'),
        path('playlist/<int:pk>/', PlayListDetails.as_view(), name='playlist details'),
        path('playlist/edit/<int:pk>/<slug:slug>', EditPlayList.as_view(), name='edit playlist'),
        path('playlist/delete/<int:pk>/<slug:slug>/', DeletePlayList.as_view(), name='delete playlist'),

        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
