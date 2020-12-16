from django.shortcuts import render, get_object_or_404

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