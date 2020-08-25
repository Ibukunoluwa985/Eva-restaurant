from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
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

def contact_us_email(request):
    context = {}
    context['menu'] = Menu.objects.order_by('-id')[:6]

    # checking if user is staff already
    if request.user.is_staff:
        messages.error(request, "You are staff. can't view user's page")
        return redirect('/staff')

    # checking if post
    if request.method == 'POST':
        # get the values from post
        receiver_email = request.POST['email']
        from_email = settings.EMAIL_HOST_USER
        subject = request.POST['email']
        message = request.POST['message']

        # sending email
        send_mail(
            subject, # subject
            message, # message
            receiver_email, # from email
            [from_email,], # to email
            fail_silently=False
        )
        # success message
        messages.success(request, "Email received! Thank's for contacting us")

        return redirect('/')

    else:
        context['chef'] = Chef.objects.order_by('-id')
        return render(request, 'index.html', context)