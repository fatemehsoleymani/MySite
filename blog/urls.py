from django.urls import path
from . import views, templatetags
from .feeds import LatestPostsFeed
app_name = 'blog'

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    # path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/<int:post_id>/share/', views.post_share, name='post_share'),
    path('posts/<int:post_id>/comment/', views.post_comment, name='post_comment'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search')
]