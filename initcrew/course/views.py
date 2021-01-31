from django.shortcuts import render,redirect
from .models import Courses
from accounts.models import ExtendedUser
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.
def course(request):
    course = Courses.objects.order_by('-created_date').filter(is_featured=True)
    data = {
        'course':course,
    }
    return render(request,'course/course.html',data)

@login_required(login_url='login')
def course_details(request,id):
    pc = ExtendedUser.objects.order_by('-created_date').filter(is_purchased=True)
    if pc:
        cours = get_object_or_404(Courses, pk=id)
        data = {
            'cours':cours,
            }
        return render(request,'course/course_detail.html',data)
    else:
        cours = get_object_or_404(Courses, pk=id)
        data = {
            'cours':cours,
            }
        return render(request,'course/course_d.html',data)





