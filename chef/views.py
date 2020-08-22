from django.shortcuts import render
from .models import Chef

# Create your views here.

def index(request):
    context = {}
    context['chef'] = Chef.objects.all()
    return render(request, 'chef/index.html', context)