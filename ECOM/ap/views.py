from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def loginUser(request):
    # return HttpResponse('Login User')
    # return render(request, 'ap/login.html')

    page = 'login'

    if request.user.is_authenticated:
        return redirect('index')


    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']


        # IF the username exists authenticate the username and password
        try:
            user = User.objects.get(username=user)
        except:
            pass

        user = authenticate(request, username=username, password=password)

        # IF the user exists login the user
        if user is not None:
            login(request, user)
        else:
            pass

        return redirect(request.GET['next'] if 'next' in request.GET else 'index')
    return render(request, 'ap/login.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')


def registerUser(request):
    # return HttpResponse('Registration User')
    return render(request, 'ap/register.html')