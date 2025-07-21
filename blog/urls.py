from django.urls import path
from blog.views import blog_view, blog_single,blog_search

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('<int:pid>', blog_single, name='single'),
    path('category/<str:cat_name>', blog_view, name='category'),
    path('tag/<str:tag_name>',blog_view,name='tag'),
    path('author/<str:author_username>', blog_view, name='author'),
    # path('test',test,name='test'),
    path('search/',blog_search,name='search'),


]

    # path('blog/<int:pk>/', counted_views.blog_single, name='blog_single'),
    # path('/single-<int:pid>/', blog_single, name='single'),
    # path('post-<int:pid>', test, name='test')


