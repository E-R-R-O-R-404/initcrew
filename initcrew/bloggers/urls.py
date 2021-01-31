from django.urls import path
from . import views


urlpatterns = [
    path('' ,views.bloggers, name="bloggers"),
    path('<int:id>' ,views.blog_details, name="blog_details"),
]