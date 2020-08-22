# importing required tools
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Menu, DeliveryLocation, Reservation
import datetime

# Create your views here.
# (NOTICE: Ignore the error on models that has no object members)

# menu home page
def index(request):
    context = {}
    context['menu'] = Menu.objects.order_by('-id')[:50]

    # checking if user is staff already
    if request.user.is_staff:
        messages.error(request, "You are staff. can't view user's page")
        return redirect('/staff')
    else:
        return render(request, 'menu/index.html', context)

# quick menu home page
def quickmenu(request):
    context = {}
    # context['menu'] = Menu.objects.filter(added_on__startswith=datetime.date.today())

    # checking if user is staff already
    if request.user.is_staff:
        messages.error(request, "You are staff. can't view user's page")
        return redirect('/staff')
    else:
        context['menu'] = Menu.objects.order_by('-id')[:50]
        return render(request, 'menu/quickmenu.html', context)

# quick menu home page
def reservation(request):
    # checking if user is staff already
    if request.user.is_staff:
        messages.error(request, "You are staff. can't view user's page")
        return redirect('/staff')
    else:
        # checking if post
        if request.method == 'POST':
            if request.POST.get('full_name') and request.POST.get('number_of_person') and request.POST.get('phone_number') and request.POST.get('email'):
                # get the values from post
                full_name = request.POST.get('full_name')
                number_of_person = request.POST.get('number_of_person')
                phone_number = request.POST.get('phone_number')
                email = request.POST.get('email')

                # sending reservation
                reservation = Reservation()
                reservation.full_name = full_name
                reservation.number_of_person = number_of_person
                reservation.phone_number = phone_number
                reservation.email = email
                reservation.save()

                # success message
                messages.success(request, "Reservation received. Will receive a call soon")
                return redirect('/menu/reservation')

            else:
                # error message
                messages.error(request, "Reservation not sent, please try later")
                return redirect('/menu/reservation')
        else:
            return render(request, 'menu/reservation.html')

# single menu data info
def show(request, id):
    context = {}
    context['menu_data'] = Menu.objects.get(id = id)
    context['menu'] = Menu.objects.order_by('-id')

    # checking if user is staff already
    if request.user.is_staff:
        messages.error(request, "You are staff. can't view user's page")
        return redirect('/staff')
    else:
        return render(request, 'menu/show.html', context)

# delivery view handler
def delivery_location(request):
        # checking if user is staff already
    if request.user.is_staff:
        messages.error(request, "You are staff. can't view user's page")
        return redirect('/staff')
    else:
        # checking if post
        if request.method == 'POST':
            if request.POST.get('number_of_plate') and request.POST.get('delivery_location'):
                # get the values from post
                number_of_plate = request.POST.get('number_of_plate')
                delivery_location = request.POST.get('delivery_location')
                ordering_plate = request.POST.get('ordering_plate')
                phone_number = request.POST.get('phone_number')

                # sending location
                location = DeliveryLocation()
                location.ordering_plate = ordering_plate
                location.phone_number = phone_number
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