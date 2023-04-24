from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm


def city_list(request):
    cities = City.objects.all()
    return render(request, 'cities/city_list.html', {'cities': cities})


def city_create(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('city_list')
    else:
        form = CityForm()
    return render(request, 'cities/city_create.html', {'form': form})


def city_update(request, pk):
    city = City.objects.get(pk=pk)
    if request.method == 'POST':
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            return redirect('city_list')
    else:
        form = CityForm(instance=city)
    return render(request, 'cities/city_update.html', {'form': form})


def city_delete(request, pk):
    city = City.objects.get(pk=pk)
    city.delete()
    return redirect('city_list')

def add_city(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CityForm()
    
    return render(request, 'add_city.html', {'form': form})