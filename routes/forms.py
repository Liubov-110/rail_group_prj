from django import forms
from .models import Route, City

class RouteForm(forms.ModelForm):
    start_city = forms.ModelChoiceField(queryset=City.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-select'}),
                                        label='Початковий населений пункт')
    end_city = forms.ModelChoiceField(queryset=City.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-select'}),
                                      label='Кінцевий населений пункт')
    travel_time = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
                                      label='Максимальний час у дорозі')
    intermediate_cities = forms.ModelMultipleChoiceField(queryset=City.objects.all(),
                                                         widget=forms.SelectMultiple(attrs={'class': 'form-select'}),
                                                         label='Проміжні населені пункти',
                                                         required=False)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                            label='Назва маршруту')

    class Meta:
        model = Route
        fields = ['start_city', 'end_city', 'travel_time', 'intermediate_cities', 'name']
