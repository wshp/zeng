from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
    po=Post.objects.all()
    return render(request,"index.html",{'po':po})


def post_list(request,id):
    post=Post.objects.get(id=id)
    return render(request,'post_list.html',{'post':post})