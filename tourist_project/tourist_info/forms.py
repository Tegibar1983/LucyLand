from django import forms
from .models import TouristInfo

class TouristInfoForm(forms.ModelForm):
    region_number=forms.CharField(max_length=50, label= "", widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Region Number'}))
    region_name=forms.CharField(max_length=50, label= "", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Region Name'}))
    map=forms.ImageField(label= "", widget=forms.FileInput(attrs={'class':'form-control', 'placeholder' : 'Map'}))
    capital_city=forms.CharField(max_length=50, label= "", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Capital City'}))
    telephone=forms.CharField(max_length=50, label= "", widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder' : 'Contact Number'}))
    email=forms.CharField(max_length=50, label= "", widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder' : 'Email'}))
    website=forms.CharField(max_length=50, label= "", widget=forms.URLInput(attrs={'class':'form-control', 'placeholder' : 'Website'}))
    class Meta:
        model = TouristInfo
        fields = '__all__'

