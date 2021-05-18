from django.contrib.auth import authenticate
from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import ProfileCreationForm

# Create your views here.
def SignUp(request):
    form = ProfileCreationForm()
    if request.method == "POST":
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            form.save()

            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user.is_authenticated():
                login(request, user)
                return redirect('events:coordinator-dashboard')
            else:
                messages.error(request, "Invalid Credentionals")
    else:
        form = ProfileCreationForm()
    return render(request, 'accounts/register.html', {'form':form})

def LogIn(request):
    return render(request, 'accounts/login.html')