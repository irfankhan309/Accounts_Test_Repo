from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
# usrphn = request.POST['unp']
# if usrphn:
#     match = User.objects.filter(Q(username__exact=usrphn)|Q(email__iexact=usrphn))


@cache_control(no_cache=True,private=True, must_revalidate=True, no_store=True)
@ensure_csrf_cookie
def Login_view(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # auth.login(request, user)
                    messages.success(request,'you are  logged in')
                    return redirect('secure')

            else:
                messages.error(request,'invalid credentials')
                return redirect('home')
        else:
            return render(request,'Accounts/login.html')

@cache_control(no_cache=True,private=True, must_revalidate=True, no_store=True)
@login_required(login_url='Login')
def logout(request):
    auth.logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('Login')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
        else:
            print('not matched password')
        return redirect('home')
    else:
        return render(request, 'Accounts/register.html')
