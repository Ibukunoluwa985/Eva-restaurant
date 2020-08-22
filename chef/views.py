# importing required tools
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Chef

# Create your views here.
# (NOTICE: Ignore the error on models that has no object members)

# chef home page
def index(request):
    context = {}
    context['chef'] = Chef.objects.all()
    
    # checking if user is staff already
    if request.user.is_staff:
        messages.error(request, "You are staff. can't view user's page")
        return redirect('/staff')
    else:
        return render(request, 'chef/index.html', context)