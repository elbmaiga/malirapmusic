from django.shortcuts import render

# Create your views here.
from articles.views import *
def index(request):
    articles = Articles.objects.all().order_by('-created_at')
    datas = {
        'articles': articles,
    }
    return render(request, 'store/index.html', datas)