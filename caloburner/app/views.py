from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Functions based views

# User Registration


def register_user(request):
    form = UserCreationForm()
    context = {'page': 'register', 'form': form}

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

    return render(request, 'registration/login.html', context)


# Function to access the frontend
def frontend(request):
    return render(request, 'frontend.html')


# Function to access the backend
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def backend(request):
    return render(request, 'backend.html')
