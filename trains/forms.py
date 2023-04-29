from django import forms
from .models import Train

class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = ['name', 'from_city', 'to_city', 'travel_time']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'from_city': forms.Select(attrs={'class': 'form-control'}),
            'to_city': forms.Select(attrs={'class': 'form-control'}),
            'travel_time': forms.NumberInput(attrs={'class': 'form-control'}),
        }
