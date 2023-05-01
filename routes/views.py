from django.shortcuts import render, get_object_or_404
from .models import Route


def route_search(request):
    if request.method == 'POST':
        start_city = request.POST['start_city']
        end_city = request.POST['end_city']
        travel_time = request.POST['travel_time']
        try:
            routes = Route.objects.filter(start_city=start_city, end_city=end_city, travel_time__lte=travel_time).order_by('travel_time')
            return render(request, 'route_results.html', {'routes': routes})
        except Route.DoesNotExist:
            message = 'Маршруту, що відповідає умовам пошуку, не існує'
            return render(request, 'route_search.html', {'message': message})
    else:
        return render(request, 'route_search.html')

def route_detail(request, pk):
    route = get_object_or_404(Route, pk=pk)
    return render(request, 'route_detail.html', {'route': route})

def route_results(request):
    routes = Route.objects.order_by('travel_time')
    return render(request, 'route_results.html', {'routes': routes})
