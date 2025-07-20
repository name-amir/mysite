from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.

def blog_view(request,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') is not None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') is not None:
        posts = posts.filter(author__username=kwargs['author_username'])
    posts = Paginator(posts, 2)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request,pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts,pk=pid)
    context = {'post':post}
    return render(request, 'blog/blog-single.html',context)


# # def test(request,name,family_name,age):
# def test(request):
#     return render(request, 'test.html')
    # post = Post.objects.get(id=pid)
    # post = get_object_or_404(Post,pk=pid)
    # context = {'post':post}

def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(conttent__contains=s)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)