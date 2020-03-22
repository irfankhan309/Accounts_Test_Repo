from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'TestApp/home.html')

@login_required(login_url='Login')
def secure(request):
    return render(request,'TestApp/secure.html')
    
@login_required(login_url='Login')
def profile(request):
    return render(request,'TestApp/profile.html')
