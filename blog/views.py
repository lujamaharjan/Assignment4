from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from . models import Blog, Author


def home(request):
    return render(request, 'blog/index.html')


def blog_list(request):
    blogs = Blog.objects.all().order_by('-id')
    print(blogs)
    paginator = Paginator(blogs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"blogs": page_obj}
    return render(request, 'blog/bloglist.html', context)


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    context = {'blog': blog}
    return render(request, 'blog/blogdetail.html', context)