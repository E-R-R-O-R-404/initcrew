from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Sliders , Navlinks , SecurityText , IndroductionBackend 
from .models import ContactUs
import bleach
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.http import require_GET
# Create your views here.

def home(request):
    sliders = Sliders.objects.all()
    navlinks = Navlinks.objects.order_by()
    indroductions = IndroductionBackend.objects.all()
    data = {
        'sliders': sliders,
        'navlinks': navlinks,
        'indroductions': indroductions,
    }
    return render(request,'webpages/home.html', data)


def security1(request):
    security1 = SecurityText.objects.all()
    data = {
        'security1' : security1,
    }
    return render(request,'webpages/security.html', data)


def contactus(request):
    if request.method == 'POST':
        full_name = bleach.clean(request.POST['full_name'])
        subject = bleach.clean(request.POST['subject'])
        phone =  bleach.clean(request.POST['phone'])
        email1 = request.POST['email']
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
        message = bleach.clean(request.POST['message'])
        user_id =  bleach.clean(request.POST['user_id'])
        
        contactus = ContactUs(full_name=full_name,subject=subject,phone=phone,email=email,message=message,user_id=user_id)
        contactus.save()
        messages.success(request , 'Thanks For Reaching Out :)')
        return redirect('/')







    



