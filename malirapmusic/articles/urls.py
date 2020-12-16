from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, kwargs={}, name='index'),
    path('<slug:param>', views.detail, kwargs={}, name='detail'),
]