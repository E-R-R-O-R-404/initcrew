from django.urls import path
from . import views

urlpatterns = [
    path('' ,views.course, name="course"),
    path('<int:id>' ,views.course_details, name="course_details"),
]
