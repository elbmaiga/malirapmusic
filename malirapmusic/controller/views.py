from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
# Create your views here.

def dashbord(request):
    return  render(request, 'controller/login.html')
    #return render(request, 'layouts/default-admin.html')

def cont(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'layouts/default-admin.html')
    else:
        # Return an 'invalid login' error message.
        return HttpResponse("No connected")