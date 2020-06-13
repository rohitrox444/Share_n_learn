from django.urls import path
from . import views

urlpatterns =[
    path('',views.showBlogs,name="blog-home"),
]
