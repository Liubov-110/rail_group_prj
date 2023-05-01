from django.shortcuts import render, redirect
from .models import SavedRoute
from .forms import SavedRouteForm

def savedroute_list(request):
    savedroutes = SavedRoute.objects.all()
    return render(request, 'savedroute_list.html', {'savedroutes': savedroutes})

def savedroute_detail(request, pk):
    savedroute = SavedRoute.objects.get(pk=pk)
    return render(request, 'savedroute_detail.html', {'savedroute': savedroute})

def savedroute_new(request):
    if request.method == "POST":
        form = SavedRouteForm(request.POST)
        if form.is_valid():
            savedroute = form.save(commit=False)
            savedroute.save()
            return redirect('savedroute_detail', pk=savedroute.pk)
    else:
        form = SavedRouteForm()
    return render(request, 'savedroute_form.html', {'form': form})

def savedroute_edit(request, pk):
    savedroute = SavedRoute.objects.get(pk=pk)
    if request.method == "POST":
        form = SavedRouteForm(request.POST, instance=savedroute)
        if form.is_valid():
            savedroute = form.save(commit=False)
            savedroute.save()
            return redirect('savedroute_detail', pk=savedroute.pk)
    else:
        form = SavedRouteForm(instance=savedroute)
    return render(request, 'savedroute_form.html', {'form': form})

def savedroute_delete(request, pk):
    SavedRoute.objects.filter(pk=pk).delete()
    savedroutes = SavedRoute.objects.all()
    return render(request, 'savedroute_list.html', {'savedroutes': savedroutes})
