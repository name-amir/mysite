from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.db.models import F


# Create your views here.

def blog_view(request):
    current_time = timezone.now()
    posts = Post.objects.filter(published_date__lte=current_time)
    return render(request, 'blog/blog-home.html', {'posts': posts})

def blog_single(request):

    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date').first()
    if post:
        post.counted_views += 1
        post.save()
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)


# def test(request,name,family_name,age):
def test(request,pid):
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post,pk=pid)
    context = {'post':post}
    
    return render(request, 'test.html', context)