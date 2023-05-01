from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import RouteForm
from .models import Route, Train, City

class RouteSearchView(FormView):
    form_class = RouteForm
    template_name = 'route_search.html'
    success_url = reverse_lazy('route_search')

    def form_valid(self, form):
        start_city = form.cleaned_data['start_city']
        end_city = form.cleaned_data['end_city']
        max_travel_time = form.cleaned_data['max_travel_time']
        intermediate_cities = form.cleaned_data['intermediate_cities']
        directions = form.cleaned_data['directions']

        # Пошук міст за іменами
        start_city_obj = City.objects.get(name=start_city)
        end_city_obj = City.objects.get(name=end_city)
        intermediate_cities_obj = [City.objects.get(name=city) for city in intermediate_cities]

        # Формування умов пошуку поїздів
        train_conditions = {
            'start_city': start_city_obj,
            'end_city': end_city_obj,
            'travel_time__lte': max_travel_time,
        }
        if directions:
            train_conditions['direction'] = directions

        if intermediate_cities_obj:
            train_conditions['mid_cities__contains'] = intermediate_cities_obj

        # Пошук поїздів зі встановленими умовами
        trains = Train.objects.filter(**train_conditions)

        # Формування маршрутів за допомогою поїздів
        routes = []
        for train in trains:
            mid_cities = train.mid_cities.split(',') if train.mid_cities else []
            route = Route(train=train, start_city=start_city_obj, end_city=end_city_obj, mid_cities=mid_cities)
            routes.append(route)

        return render(self.request, self.template_name, {'form': form, 'routes': routes})
