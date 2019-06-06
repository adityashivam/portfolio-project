from django.shortcuts import render
from .models import Blog

def blog(request):

    return render(request,'blog/blog.html')
