from django import forms
from radio.models import RadioStation


class RadioStationCreateForm(forms.ModelForm):
    class Meta:
        model = RadioStation
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'radio-name'})
        }


class RadioStationDisplayForm(forms.Form):
    pass