from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, kwargs={}, name='index'),
    path('<slug:param>', views.detail, kwargs={}, name='detail'),
    path('search/<slug:param>', views.search, kwargs={}, name='search'),
    path('search/', views.search_form, kwargs={}, name='search_form')
]