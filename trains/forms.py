from django import forms
from .models import Train

class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = ['code', 'start_city', 'end_city', 'travel_time']

        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'start_city': forms.Select(attrs={'class': 'form-control'}),
            'end_city': forms.Select(attrs={'class': 'form-control'}),
            'travel_time': forms.NumberInput(attrs={'class': 'form-control'}),
        }
