from django.shortcuts import render, get_object_or_404, redirect
from .models import Train
from .forms import TrainForm

def train_list(request):
    trains = Train.objects.all()
    return render(request, 'trains/train_list.html', {'trains': trains})

def train_detail(request, pk):
    train = get_object_or_404(Train, pk=pk)
    return render(request, 'trains/train_detail.html', {'train': train})

def train_add(request):
    if request.method == 'POST':
        form = TrainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('train_list')
    else:
        form = TrainForm()
    return render(request, 'trains/train_form.html', {'form': form})

def train_edit(request, pk):
    train = get_object_or_404(Train, pk=pk)
    if request.method == 'POST':
        form = TrainForm(request.POST, instance=train)
        if form.is_valid():
            form.save()
            return redirect('train_list')
    else:
        form = TrainForm(instance=train)
    return render(request, 'trains/train_form.html', {'form': form})

def train_delete(request, pk):
    train = get_object_or_404(Train, pk=pk)
    train.delete()
    return redirect('train_list')
