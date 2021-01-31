from django.shortcuts import render
from .models import Bloggers
from django.shortcuts import get_object_or_404

# Create your views here.

def bloggers(request):
    blogs = Bloggers.objects.order_by('-created_date').filter(is_featured=True)
    data = {
        'blogs':blogs,
    }
    return render(request ,'bloggers/blogs.html',data)


def blog_details(request, id):
    blog = get_object_or_404(Bloggers, pk=id)
    data = {
        'blog':blog,
    }
    return render(request ,'bloggers/blogs_details.html',data)