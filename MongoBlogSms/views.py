from django.shortcuts import render, redirect, HttpResponse
from Model.models import *


# Create your views here.

def HomePage(request):
    r_posts = Post.objects.all().order_by('-id')[:3]
    return render(request,'MongoBlogSms/index.html',locals())