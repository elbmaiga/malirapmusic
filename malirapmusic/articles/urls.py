from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, kwargs={}, name='index'),
    path('<slug:param>', views.detail, kwargs={}, name='detail'),
    path('category/<slug:param>', views.find_category, kwargs={}, name='find_category'),
    path('search/', views.search, kwargs={}, name='search'),
]