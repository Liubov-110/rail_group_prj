from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm


def user_profile_detail(request, pk):
    user_profile = get_object_or_404(UserProfile, pk=pk)
    context = {'user_profile': user_profile}
    return render(request, 'user_profile_detail.html', context)

def user_profile_create(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save()
            return redirect('user_profile_detail', pk=user_profile.pk)
    else:
        form = UserProfileForm()
    context = {'form': form}
    return render(request, 'user_profile_form.html', context)

def user_profile_edit(request, pk):
    user_profile = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            user_profile = form.save()
            return redirect('user_profile_detail', pk=user_profile.pk)
    else:
        form = UserProfileForm(instance=user_profile)
    context = {'form': form}
    return render(request, 'user_profile_form.html', context)

def user_profile_delete(request, pk):
    user_profile = get_object_or_404(UserProfile, pk=pk)
    user_profile.delete()
    return redirect('user_profile_list')

def user_profile_list(request):
    user_profiles = UserProfile.objects.all()
    context = {'user_profiles': user_profiles}
    return render(request, 'user_profile_list.html', context)
