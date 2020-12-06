from django.forms import ModelForm, TextInput
from profiles.models import UserProfile


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        widgets = {

        }


