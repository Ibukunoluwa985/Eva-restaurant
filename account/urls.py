# importing required tools
from django.urls import path, include
from . import views

# Each URL actual path with be commented above it.

urlpatterns = [
    # path to "<website>/account/" e.g = www.eva.com/account/
    path('', views.index, name='index'),

    # path to "<website>/account/login" e.g = www.eva.com/account/login
    path('login', views.user_login, name='login'),

    # path to "<website>/account/logout" e.g = www.eva.com/account/logout
    path('logout', views.user_logout, name='logout'),

    # path to "<website>/account/register" e.g = www.eva.com/account/register
    path('register', views.user_register, name='register'),

    # path to "<website>/account/delect" e.g = www.eva.com/account/delect
    path('delect', views.delect_account, name='delect'),
]