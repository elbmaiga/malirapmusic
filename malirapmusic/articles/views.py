from django.shortcuts import render, get_object_or_404, HttpResponse
from django.db.models import Q
from .models import *
# Create your views here.

def index(request):
    articles = Articles.objects.all().order_by('-created_at')
    isActive = True
    datas = {
        'articles': articles,
        'active': isActive
    }
    return render(request, 'articles/index.html', datas)

def detail(request, param):
    #articles = Articles.objects.get(slug=param)
    article = get_object_or_404(Articles, slug=param)
    article.views += 1
    article.save()

    datas = {
        'article': article
    }
    return render(request, 'articles/detail.html', datas)

def find_category(request, param):
    if param == 'singles':
        page = 'articles/single.html'
    elif param == 'videos':
        page = 'articles/video.html'
    elif param == 'downloads':
        page = 'articles/download.html'
    elif param == 'albums':
        page = 'articles/album.html'
    elif param == 'actu-buzz':
        page = 'articles/actu_buzz.html'
    else:
        page = 'articles/search.html'

    articles = Articles.objects.filter(Q(title__icontains=param) | Q(category__fields__icontains=param))
    datas = {
        'results': articles
    }
    return render(request, page, datas)

def search(request):
    context = request.GET['s']
    result = Articles.objects.filter(Q(title__icontains=context) | Q(category__fields__icontains=context))
    datas = {
        'results': result,
        'context': context
    }
    return render(request, 'articles/search.html', datas)

def gallery(request):
    queryset = Galleries.objects.all().order_by('-created_at')
    datas = {
        'galleries': queryset,
    }
    return render(request, 'articles/gallery.html', datas)
