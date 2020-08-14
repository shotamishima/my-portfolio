from django.shortcuts import render

from .models import Blog

def allblog(request):
	blogs = Blog.objects
	return render(request, 'blogs/allblogs.html', {'blogs':blogs})