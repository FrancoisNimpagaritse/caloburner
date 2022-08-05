from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required

# Functions based views


# Function to access the frontend
def frontend(request):
    return render(request, 'frontend.html')


# Function to access the backend
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def backend(request):
    return render(request, 'backend.html')
