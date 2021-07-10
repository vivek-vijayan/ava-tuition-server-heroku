from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def AVA_login(request):
    if request.user.is_authenticated:
        return render(request, "AVA-message-display.html", {'username': request.user, 'message': "Authenticated successfully"})
    else:
        return render(request, "AVA-login.html", {})


def AVA_logginer(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user:
        if user:
            login(request, user)
            return render(request, "AVA-message-display.html", {'username': request.user, 'message': "Login successful"})
        # checking access to A2Portal
        
    else:
        return render(request, "AVA-login.html", {'error': 'Invalid credentials', 'iserror': True})


@login_required(login_url=AVA_login)
def AVA_Home(request):
    fullname = str(request.user.first_name)  + " " + str(request.user.last_name)
    return render(request, "AVA-home.html",{
        'username': request.user,
        'fullname' : fullname,
    })


def AVA_logout(request):
    logout(request)
    return redirect(AVA_login)
