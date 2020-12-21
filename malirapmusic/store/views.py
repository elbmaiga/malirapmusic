from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from articles.views import *
def index(request):
    ARTICLE_PER_PAGE = 20
    articles = Articles.objects.all().order_by('-created_at')
    most_views = Articles.objects.all().order_by('-views')[:6]
    paginator = Paginator(articles, ARTICLE_PER_PAGE)
    page_number = request.GET.get('page')
    if not page_number:
        page_number = 1
    page_obj = paginator.get_page(page_number)
    datas = {
        'title': 'store',
        'articles': paginator.page(page_number),
        'page_obj': page_obj,
        'most_views': most_views
    }
    return render(request, 'store/index.html', datas)