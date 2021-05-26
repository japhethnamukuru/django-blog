from django.core import paginator
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView  

from .models import Post

def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) #3 posts in every page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        #if page not an integer deliver the first page 
        posts = paginator.page(1)
    except EmptyPage:
        #if page is out of range deliver last result
        posts = paginator.page(paginator.num_pages)

    return render(request, 'content/index.html', {'page':page, 'posts':posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year,
    publish__month=month, publish__day=day)

    return render(request, 'content/detail.html', {'post':post})    