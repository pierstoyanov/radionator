from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from common.BackgroundMixin import BackgroundMixin
from common.CookieTestResultMixin import CookeTestResultMixin
from common.CookieTestStageMixin import CookieTestStageMixin
from radionator.radio.forms.radio_forms import RadioStationCreateForm
from radionator.radio.models import RadioStation

RadioUser = get_user_model()


class AddRadio(BackgroundMixin,
               LoginRequiredMixin,
               CookeTestResultMixin,
               CookieTestStageMixin,
               CreateView):
    """View to create an new RadioStation object"""
    model = RadioStation
    form_class = RadioStationCreateForm
    template_name = 'radio/radio_add.html'
    success_url = reverse_lazy('radio index')


class RadioDetails(BackgroundMixin,
                   CookeTestResultMixin,
                   CookieTestStageMixin,
                   DetailView):
    """View to display a RadioStation object.
    This leads to EDIT AND DELETE views for elevated users only"""
    model = RadioStation
    template_name = 'radio/radio_details.html'
    context_object_name = 'station'
    # queryset = RadioStation.objects.all()
    #
    # def get_context_data(self, *args, **kwargs):
    #     context = super(RadioDetails, self).get_context_data(*args, **kwargs)
    #     return context


class EditRadio(BackgroundMixin,
                LoginRequiredMixin,
                CookeTestResultMixin,
                CookieTestStageMixin,
                UpdateView):
    """Edit the RadioStation object. Returns MSG if successful"""
    model = RadioStation
    fields = '__all__'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO,
                             f'Radio {self.object.name} edited successfully.')
        return reverse_lazy('radio index')


class DeleteRadio(BackgroundMixin,
                  LoginRequiredMixin,
                  CookeTestResultMixin,
                  CookieTestStageMixin,
                  DeleteView):
    """Delete the RadioStation object. Returns MSG if successful"""
    model = RadioStation

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO,
                             f'Radio {self.object.name} DELETED successfully. :(')
        return reverse_lazy('radio index')
