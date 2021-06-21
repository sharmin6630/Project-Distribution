from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import CustomUser
from django.db.models import Q
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.conf import settings
from django.contrib.auth import get_user

# Create your views here.

# def home(request):
#     return render(request, 'index.html')

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print("user", user, username, password)
        if user is not None:
            if user.is_active:
                print("ok2")
                auth_login(request, user)
                print("ok2")
                return render(request, 'teacherclick.html')
            else:
                #messages.info(request, 'invalid credentials')
                print("invalid")
                return render(request, 'home.html')
        else:
            print("ok4")
            return render(request, 'register.html')
    else:
        return render(request, 'home.html')

# def aboutus_view(request):
#     return render(request,'aboutus.html')

def contact(request):
    # sub = forms.ContactusForm()
    # if request.method == 'POST':
    #     sub = forms.ContactusForm(request.POST)
    #     if sub.is_valid():
    #         email = sub.cleaned_data['Email']
    #         name=sub.cleaned_data['Name']
    #         message = sub.cleaned_data['Message']
    #         #send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
    #         return render(request, 'quiz/contactussuccess.html')
    # return render(request, 'contact.html', {'form':sub})
    return render(request, 'contact.html')

def about(request):
    return render(request,'about.html')

def adminclick(request):
    return render(request,'index.html')

def teacherclick(request):
    return render(request,'teacherclick.html')

def studentclick(request):
    return render(request,'studentclick.html')

def register(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        username = request.POST.get('username')
        user = CustomUser(username=username, user_type=user_type, first_name=first_name, last_name=last_name, email=email, password1=password1)
        print("user created")
        user.set_password(password)
        user.is_active = True
        user.save()
        return redirect('/')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("ok")
        user = authenticate(username=username, password=password)
        print("usser", user)
        if user is not None:
            if user.is_active:
                print("ok2")
                auth_login(request, user)
                print("ok2")
                return render(request, 'teacherclick.html')
            else:
                #messages.info(request, 'invalid credentials')
                print("invalid")
                return render(request, 'home.html')
        else:
            print("ok4")
            return render(request, 'register.html')
    else:
        return render(request, 'home.html')