from django.shortcuts import render
from blog.models import blog_list
# Create your views here.

def showBlogs(request):
    blog_list_data = blog_list.objects.all()
    return render(request,'blog-page.html',{'blog_list_data':blog_list_data})
