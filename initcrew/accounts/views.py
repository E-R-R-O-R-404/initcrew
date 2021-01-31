from django.shortcuts import render, redirect
from django.contrib.auth import logout , login
from django.contrib.auth.models import User
from django.contrib import messages,auth
from .models import ExtendedUser
from django.contrib.auth.decorators import login_required
import bleach

# Create your views here.
def login(request):

     if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']
         if len(password) > 50:
             messages.warning(request, 'Detected malicious Attempt :(')
             return redirect('security1')
         else:
             user1 = auth.authenticate(username=username,password=password)
             if user1 is not None:
                 auth.login(request,user1)
                 messages.success(request, 'You are Logged in :)')
                 return redirect('/')
             else:
                 messages.warning(request, 'Invalid Credentials')
                 return redirect('login')

     return render(request,'account/login.html')


def register(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        username = bleach.clean(username1)
        email1 = request.POST['email']

        #sanitize email code
        def sanitize(email1):
            email = ''
            for i in email1:
                if i == '>':
                    outchar = '&gt;'
                elif i == '<':
                    outchar = '&lt;'
                elif i == '(':
                    outchar = '%28'
                elif i == ')':
                    outchar = '%29'
                elif i == '[':
                    outchar = '%5B'
                elif i == '}':
                    outchar = '%7D'
                elif i == "'":
                    outchar = 'co@ma'
                elif i == '=':
                    outchar = 'eql2'
                elif i == '#':
                    outchar = '%23'
                elif i == '+':
                    outchar = '%2B'
                elif i == "-":
                    outchar = 'm1nu5'
                else:
                    outchar = i
                email += outchar
            return email


        email = sanitize(email1)
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if len(password) > 30:
            messages.warning(request, 'malicious logged')
            return redirect('security1')
        else:
            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.warning(request, 'Username Already exist')
                    return redirect('register')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.warning(request, 'Email already exist')
                        return redirect('register')
                    else:
                        user = User.objects.create_user(username=username, email=email, password=password)
                        user.save()
                        phone_num = bleach.clean(request.POST['phone_num'])
                        newextendeduser = ExtendedUser(phone_num=phone_num, user=user)
                        newextendeduser.save()
                        messages.success(request, 'Account created succesfully')
                        return redirect('login')
                        
            else:
                messages.error(request, 'Password do not match')
                return redirect('register')
        
    return render(request,'account/signup.html')


def logout_user(request):
    logout(request)
    return redirect('/')

    