from django.db import models

# Create your models here.
class Category(models.Model):
    category_text = models.CharField(max_length=30)

class Post(models.Model):
    title = models.CharField(max_length=30),
    body = models.TextField(),
    created_on = models.DateTimeField(auto_now_add=True),
    last_modified = models.DateTimeField(auto_now=True),
    category_choose = models.ManyToManyField('Category',related_name='posts')

class Comment(models.Model):
    author = models.CharField(max_length=30),
    body = models.TextField(),
    created_on = models.DateTimeField(auto_now_add=True),
    post = models.ForeignKey('Post',on_delete=models.CASCADE)
