from django.contrib import admin
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostView, ProfileView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='projects-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostUpdateView.as_view(), name='post-delete'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('all_posts/', PostView.as_view(), name='allposts'),
    path('all_profile/', ProfileView.as_view(), name='allprofile'),
]
