from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/email', views.contact_us_email, name='contact_us_email'),
]