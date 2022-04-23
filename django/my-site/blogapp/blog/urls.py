from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('index',views.index),
    path('blogs',views.blogs,name='blogs'),
    path('blogs/<slug:slug>',views.blogdetails,name='blog_details'),
    path('category/<slug:slug>',views.blogsByCategory,name='blogs_by_category')
]