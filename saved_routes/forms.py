from django import forms
from .models import SavedRoute

class SavedRouteForm(forms.ModelForm):
    class Meta:
        model = SavedRoute
        fields = ['name', 'route']
