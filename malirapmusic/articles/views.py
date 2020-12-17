from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import *
# Create your views here.

def index(request):
    articles = Articles.objects.all()
    datas = {
        'articles': articles
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

def search(request, param):
    result = Articles.objects.filter(Q(title__icontains=param) | Q(category__fields__icontains=param))
    datas = {
        'results': result
    }
    return render(request, 'articles/search.html', datas)

def search_form(request):
    context = request.GET['s']
    result = Articles.objects.filter(Q(title__icontains=context) | Q(category__fields__icontains=context))
    datas = {
        'results': result,
        'context': context
    }
    return render(request, 'articles/search.html', datas)