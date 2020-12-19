from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashbord, kwargs={}, name='dashbord')
]