# importing required tools
from django.urls import path, include
from . import views

# Each URL actual path with be commented above it.

urlpatterns = [
    # path to "<website>/chef/" e.g = www.eva.com/chef/
    path('', views.index, name='index'),
]