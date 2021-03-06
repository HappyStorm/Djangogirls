# trips/views.py

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#E:\Github\Djangogirls\mysite

#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#E:\Github\Djangogirls\mysite\trips

#BASE_DIR = os.path.dirname(os.path.realpath(__file__))
#E:\Github\Djangogirls\mysite\trips

#BASE_DIR = os.path.abspath(os.path.dirname(__file__))
#E:\Github\Djangogirls\mysite\trips

#BASE_DIR = os.path.realpath(os.path.dirname(__file__))
#E:\Github\Djangogirls\mysite\trips

#BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#E:\Github\Djangogirls\mysite

#TEMPLATE_DIRS = (
 #   os.path.join(BASE_DIR, 'templates').replace('\\', '/'),
#)
#E:/Github/Djangogirls/mysite/templates

#TEMPLATE_DIRS = (
 #   os.path.join(BASE_DIR, 'templates'),
#)
#E:\Github\Djangogirls\mysite\templates

from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from trips.models import Post

def hello_world(request):
    #return HttpResponse("Hello World" + "\n" + "ABC")
    #return HttpResponse(BASE_DIR)
    #return HttpResponse(TEMPLATE_DIRS)
    return render(request,
                    'hello_world.html',
                    {'current_time': datetime.now()})

def home(request):
    # get all the posts
    post_list = Post.objects.all()
    return render(request,
                    'home.html',
                    {'post_list': post_list})

def post_detail(request, id):
	post = Post.objects.get(id=id)
	return render(request, 'post.html', {'post': post})