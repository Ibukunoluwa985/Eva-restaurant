# importing required tools
from django.urls import path, include
from . import views

# Each URL actual path with be commented above it.

urlpatterns = [
    # path to "<website>/menu/" e.g = www.eva.com/menu/
    path('', views.index, name='index'),

    # path to "<website>/menu/item/<the item id>" e.g = www.eva.com/menu/item/1
    path('item/<id>', views.show, name='show'),

    # path to "<website>/menu/" e.g = www.eva.com/menu/
    path('reservation', views.reservation, name='reservation'),

    # path to "<website>/menu/quickmenu" e.g = www.eva.com/menu/quickmenu
    path('quickmenu', views.quickmenu, name='quickmenu'),

    # path to "<website>/menu/delivery/location" e.g = www.eva.com/menu/delivery/location
    path('delivery/location', views.delivery_location, name='delivery_location'),
]