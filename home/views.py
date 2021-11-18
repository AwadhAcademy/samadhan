from django.shortcuts import render, HttpResponse, redirect
from .models import quote_data
from .models import Carousel_Data
from .models import service
from .models import legal_service
from .models import tax_compliance
from .models import new_registration
from .models import bloging_data
from .models import additional_services
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,  login, logout


def base(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        quary = request.POST.get('quary')
        data = quote_data(fname=fname, phone=phone, email=email, quary=quary)
        data.save()
    photo = Carousel_Data.objects.all()
    data_service = additional_services.objects.all()
    ca_service = service.objects.all()
    legal = legal_service.objects.all()
    n = len(photo)
    photo = {'photo': photo, 'ca_service': ca_service,
             'legal': legal, 'data_service': data_service}
    return render(request, 'home/home.html', photo)


def loogin(request):
    if request.method == "POST":
        # Get the post parameters
        name = request.POST['loginusername']
        passw = request.POST['loginpassword']
        print(name)
        user = authenticate(username=name, password=passw)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            params = {'name':name}
            return render(request, 'home/loogin.html',params)
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return render(request, 'home/loogin.html')
    return render(request, 'home/loogin.html')


def qurey_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        qurey = request.POST.get('qurey')
        data = tax_compliance(name=name, phone=phone, email=email, qurey=qurey)
        data.save()
    return render(request, 'home/qurey_form.html')


def sign_up(request):
    if request.method == "POST":
        name = request.POST.get('name')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if(password1 == password2):
            data = new_registration(name=name, first_name=first_name, last_name=last_name,
                                    email=email, password1=password1, password2=password2)
            data.save()
            username = name
            password = password1
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = first_name
            myuser.last_name = last_name
            myuser.save()
        else:
            messages.warning(request, 'Password Doesnot Match')
    return render(request, 'home/sign_up.html')


def blogs(request):
    data = bloging_data.objects.all()
    length = len(data)
    print(length)
    params = {'data': data, 'length': length}
    return render(request, 'home/blogs.html', params)
# Create your views here.

def info(request):
    return render(request,'home/info.html')
def loogout(request):
    auth.logout(request)
    return render(request, 'home/loogin.html')