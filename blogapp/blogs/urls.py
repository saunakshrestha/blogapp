from django.urls import path
from . import views

urlpatterns = [
    path('',views.blogs_index,name='blogs_index'),
    path('post/<int:pk>/',views.blogs_detail,name='blogs_detail'),
    path('category/<str:category>/',views.blogs_category,name='blogs_category'),
]