from django.urls import path
from .views import PostListView, post_detail


app_name = 'blog'


urlpatterns = [
    path('', PostListView.as_view(), name='blog_list'),
    path('<slug:slug_name>/', post_detail, name='blog_detail'),

]