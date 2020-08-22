from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/<id>', views.show, name='show'),
    path('quickmenu', views.quickmenu, name='quickmenu'),
    path('delivery/location', views.delivery_location, name='delivery_location'),
]