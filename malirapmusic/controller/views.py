from django.shortcuts import render

# Create your views here.

def dashbord(request):
    return render(request, 'layouts/default-admin.html')