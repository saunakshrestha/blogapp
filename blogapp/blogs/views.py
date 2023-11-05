from django.shortcuts import render
from blogs.models import Post,Comment

# Create your views here.

def blogs_index(request):
    posts = Post.objects.all().order_by("-created_on") #-ve means big to small order
    context = {
        "posts" : posts,
    }
    return render(request,'blogs/index.html/',context)

def blogs_category(request,category):
    posts = Post.objects.filter(
        category_choose__category_text__contains = category
    ).order_by("-created_on")]
    context = {
        "category" : "category",
        "posts" : posts,
    }
    return render(request,'blogs/category.html',context)

def blogs_detail(request,pk):
    post = Post.object.get(pk=pk)
    comments = Comment.object.filter(post = post)
    context = {
        "post" :post,
        "comments":comments,
    }
    return render(request,'blogs/detail.html',context)


