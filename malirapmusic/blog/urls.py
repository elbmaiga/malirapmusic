from django.urls import path

from .import views
urlpatterns = [
    path('', views.index, kwargs={}, name='blog_index')
]