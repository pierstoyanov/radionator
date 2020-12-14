from django import forms
from radionator.radio.models import RadioStation


class RadioStationCreateForm(forms.ModelForm):
    class Meta:
        model = RadioStation
        exclude = ('slug',)
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control-sm',
                    'placeholder': 'Awesome Radio\'s name'}),
            'url': forms.URLInput(
                attrs={'class': 'col-form-label-lg',
                       'placeholder': 'Add streaming url, not the radio\'s site page!'}),
        }


class RadioStationDisplayForm(forms.Form):
    class Meta:
        model = RadioStation
        exclude = ('slug', 'url')
        widgets = {
            # 'name': forms.TextInput(attrs={'class': 'radio-name'})
        }
