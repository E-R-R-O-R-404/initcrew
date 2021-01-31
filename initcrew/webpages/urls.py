from django.urls import path
from . import views
from django.conf.urls import url
from django.http import HttpResponse

urlpatterns = [
    path('' ,views.home, name="home"),
    path('.well-known/security.txt' ,views.security1, name="security1"),
    path('contactus/',views.contactus, name="contactus") ,
    url(r'^robots.txt', lambda x: HttpResponse("User-Agent: *\nDisallow:/static/*\nDisallow:/media/*\nDisallow:/course/*", content_type="text/plain"), name="robots_file"),
    
]