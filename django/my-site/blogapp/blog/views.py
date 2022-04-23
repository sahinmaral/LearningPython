from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog,Category

def index(request):
    context = {
        'blogs':Blog.objects.filter(isHome=True,isActive=True),
        'categories': Category.objects.all()
    }
    return render(request,'blog/index.html',context)

def blogs(request):
    context = {
        'blogs':Blog.objects.filter(isActive=True),
        'categories': Category.objects.all()
    }
    return render(request,'blog/blogs.html',context)

def blogdetails(request,slug):

    blog = Blog.objects.get(slug=slug)

    return render(request,'blog/blog-details.html',
    {
        'blog' : blog
    })

def blogsByCategory(request,slug):
    context = {
        # 'blogs':Blog.objects.filter(isActive=True,category__slug = slug),
        'blogs':Category.objects.get(slug=slug).blog_set.filter(isActive=True),
        'categories': Category.objects.all(),
        'selected_category':slug
    }
    return render(request,'blog/blogs.html',context)