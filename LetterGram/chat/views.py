from django.shortcuts import render, redirect
from django.http.response import HttpResponse

def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login")
    context = {}
    return render(request, "home.html", context)

def healthcheck(request):    
    return HttpResponse('200')