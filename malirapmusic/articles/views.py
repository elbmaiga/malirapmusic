from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponse
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from .models import *
# Create your views here.

def index(request):
    ARTICLE_PER_PAGE = 1

    articles = get_list_or_404(Articles.objects.order_by('-created_at'))
    try:
        paginator = Paginator(articles, ARTICLE_PER_PAGE)
    except:
        return HttpResponse("Hello")
    page_number = request.GET.get('page')
    if not page_number:
        page_number = 1
    page_obj = paginator.get_page(page_number)
    most_views = Articles.objects.all().order_by('-views')[:6]

    datas = {
        'most_views': most_views,
        'title': 'home',
        'articles': paginator.page(page_number),
        'page_obj': page_obj,
    }
    return render(request, 'articles/index.html', datas)

def detail(request, param):
    #articles = Articles.objects.get(slug=param)
    article = get_object_or_404(Articles, slug=param)
    article.views += 1
    article.save()
    most_views = Articles.objects.all().order_by('-views')[:6]
    datas = {
        'article': article,
        'most_views': most_views
    }
    return render(request, 'articles/detail.html', datas)

def find_category(request, param):
    ARTICLE_PER_PAGE = 10
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
    most_views = Articles.objects.all().order_by('-views')[:6]
    paginator = Paginator(articles, ARTICLE_PER_PAGE)
    page_number = request.GET.get('page')
    if not page_number:
        page_number = 1
    page_obj = paginator.get_page(page_number)

    datas = {
        'title': param,
        'results': paginator.page(page_number),
        'most_views': most_views,
        'page_obj': page_obj,
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
        'title': 'galleries',
        'galleries': queryset,
    }
    return render(request, 'articles/gallery.html', datas)
