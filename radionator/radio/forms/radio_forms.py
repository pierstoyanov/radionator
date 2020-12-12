from django import forms
from radionator.radio.models import RadioStation


class RadioStationCreateForm(forms.ModelForm):
    class Meta:
        model = RadioStation
        exclude = ('slug',)


class RadioStationDisplayForm(forms.Form):
    class Meta:
        model = RadioStation
        exclude = ('slug', 'url')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'radio-name'})
        }
