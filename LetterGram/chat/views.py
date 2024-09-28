from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from .forms import UserProfileForm
from .models import UserProfile

def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login") 
    
    context = {}
    return render(request, 'home.html')

def healthcheck(request):    
    return HttpResponse('200')

@login_required
def profile(request):    

    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profile.html', {'form':form})
    