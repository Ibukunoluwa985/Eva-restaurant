from django.shortcuts import render, redirect
from django.contrib import messages
from menu.models import Menu
from chef.models import Chef
# Create your views here.

def index(request):
    context = {}
    context['menu'] = Menu.objects.order_by('-id')[:6]

    # checking if user is staff already
    if request.user.is_staff:
        messages.error(request, "You are staff. can't view user's page")
        return redirect('/staff')
    else:
        context['chef'] = Chef.objects.order_by('-id')
        return render(request, 'index.html', context)