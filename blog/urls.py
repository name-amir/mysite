from django.urls import path
from blog.views import blog_view, blog_single

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('<int:pid>', blog_single, name='single'),  
]

    # path('blog/<int:pk>/', counted_views.blog_single, name='blog_single'),
    # path('/single-<int:pid>/', blog_single, name='single'),
    # path('post-<int:pid>', test, name='test')


