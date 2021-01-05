from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    datas = {
        'title': 'blog'
    }
    return render(request, 'blog/index.html', datas)