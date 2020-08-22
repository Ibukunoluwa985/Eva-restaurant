# importing required tools
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required
from menu.models import DeliveryLocation

# Create your views here.
# (NOTICE: Ignore the error on models that has no object members)

# user account page
@login_required(login_url='/account/login')
def index(request):
    context = {}
    context['delivery'] = DeliveryLocation.objects.order_by('-id')
    return render(request, 'staff/index.html', context)