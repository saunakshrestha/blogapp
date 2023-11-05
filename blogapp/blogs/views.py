from django.http import HttpResponseRedirect
from django.shortcuts import render
from blogs.models import Post,Comment
from blogs.forms import CommentForm


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
    ).order_by("-created_on")
    context = {
        "category" : category,
        "posts" : posts,
    }
    return render(request,'blogs/category.html',context)

#get specific post with comments
def blogs_detail(request,pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                post = post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post = post)
    context = {
        "post" :post,
        "comments":comments,
        "Form":CommentForm(),
    }
    return render(request,'blogs/detail.html',context)


