from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import auth, User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.

# user account page
@login_required
def index(request):
    return render(request, 'registration/index.html')

# logging in user
def user_login(request):
    # checking if user is login already
    if request.user.is_authenticated:
        return redirect('/')
    # checking if post
    if request.method == 'POST':
        # get the values from post
        username = request.POST['username']
        password = request.POST['password']

        # making some validations
        user = auth.authenticate(username=username,password=password)

        # logging user, if logged out 
        if user is not None:
            auth.login(request, user)
            messages.success(request, "User just logged in")
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials.')
            return redirect('/account/login')
    else:
        return render(request, 'registration/login.html')

# registaring user, not using form model method
@csrf_exempt
@csrf_protect
def user_register(request):
    # checking if user is login already
    if request.user.is_authenticated:
        return redirect('/')
    # checking if post
    if request.method == 'POST':
        # get the values from post
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_cfrm = request.POST['password_cfrm']
        
        # making some validations
        if password == password_cfrm:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'User already exists.')
                return redirect('/account/register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
                return redirect('/account/register')
            # creating a user
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.save()
                # logging in user after registration
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, "User created")
                return redirect('/')
        else:
            messages.error(request, "Password don't match.")
            return redirect('/account/register')
    else:
        return render(request, 'registration/register.html')

# logging out user
@login_required(login_url='/account/login')
def user_logout(request):
    auth.logout(request)
    messages.success(request, 'You just logged out.')
    return redirect('/')