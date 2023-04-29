from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import locale


def index(request):
    cities = list(City.objects.all())
    cities.sort(key=lambda x: locale.strxfrm(x.name))
    # cities = City.objects.all()
    paginator = Paginator(cities, 10)  # 10 cities in each page
    page = request.GET.get('page')
    try:
        cities = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        cities = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        cities = paginator.page(paginator.num_pages)
    return render(request, 'cities/index.html', {'cities': cities})

def city_list(request):
    cities = City.objects.all()
    paginator = Paginator(cities, 10)  # 10 cities in each page
    page = request.GET.get('page')
    try:
        cities = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        cities = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        cities = paginator.page(paginator.num_pages)
    # return render(request, 'cities/city_list.html', {'cities': cities, 'page': page})
    return render(request, 'cities/index.html', {'cities': cities, 'page': page})


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