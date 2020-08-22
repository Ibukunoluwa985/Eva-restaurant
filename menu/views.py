from django.shortcuts import render, redirect
from .models import Menu, DeliveryLocation
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages

# Create your views here.

def index(request):
    context = {}
    context['menu'] = Menu.objects.order_by('-id')[:50]
    return render(request, 'menu/index.html', context)

def quickmenu(request):
    context = {}
    # context['menu'] = Menu.objects.filter(added_on__startswith=datetime.date.today())
    context['menu'] = Menu.objects.order_by('-id')[:50]
    return render(request, 'menu/quickmenu.html', context)

def show(request, id):
    context = {}
    context['menu_data'] = Menu.objects.get(id = id)
    context['menu'] = Menu.objects.order_by('-id')
    return render(request, 'menu/show.html', context)

def delivery_location(request):
    # checking if post
    if request.method == 'POST':
        if request.POST.get('number_of_plate') and request.POST.get('delivery_location'):
            # get the values from post
            number_of_plate = request.POST.get('number_of_plate')
            delivery_location = request.POST.get('delivery_location')

            # sending location
            location = DeliveryLocation()
            location.number_of_plate = number_of_plate
            location.delivery_location = delivery_location
            location.save()

            # success message
            messages.success(request, "Location received. Will receive a call soon")
            return redirect('/menu/')

        else:
            # error message
            messages.error(request, "Location not sent, please try later")
            return redirect('/menu/item/')
    else:
        return render(request, 'menu/show.html')