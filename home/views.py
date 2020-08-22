from django.shortcuts import render
from menu.models import Menu
from chef.models import Chef
# Create your views here.

def index(request):
    context = {}
    context['menu'] = Menu.objects.order_by('-id')[:6]

    context['chef'] = Chef.objects.order_by('-id')
    return render(request, 'index.html', context)