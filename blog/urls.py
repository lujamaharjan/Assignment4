from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs-list/', views.blog_list, name="blog_list"),
    path('blog-detail/<int:blog_id>/', views.blog_detail, name='blog_detail')
]
