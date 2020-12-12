from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from radionator.radio.models import RadioStation


class AddRadio(CreateView):
    """View to create an new RadioStation object"""
    model = RadioStation
    template_name = 'radio/radio_add.html'
    fields = '__all__'

    success_url = reverse_lazy('radio index')


class RadioDetails(DetailView):
    """View to display a Radiostation object.
    This leads to EDIT AND DELETE views for elevated users only"""
    model = RadioStation
    template_name = 'radio/radio_details.html'


#TODO Edit Delete foor elevated users only
class EditRadio(UpdateView):
    """Edit the RadioStation object. Returns MSG if successful"""
    model = RadioStation
    fields = '__all__'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO,
                             f'Radio {self.object.name} edited successfully.')
        return reverse_lazy('radio index')


class DeleteRadio(DeleteView):
    """Delete the RadioStation object. Returns MSG if successful"""
    model = RadioStation

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO,
                             f'Radio {self.object.name} DELETED successfully. :(')
        return reverse_lazy('radio index')