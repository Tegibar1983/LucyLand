from django import forms
from .models import TouristInfo

class TouristInfoForm(forms.ModelForm):
    class Meta:
        model = TouristInfo
        fields = '__all__'