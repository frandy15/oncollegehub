from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    CommentDeleteView,
                    CommentUpdateView,
                    SearchListView,
                    PostCollegeListView
                    )
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('college/<int:pk>/<str:name>/questions/',
         PostCollegeListView.as_view(), name='blog-college'),
    path('search',
         SearchListView.as_view(), name='search_list'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/<title>/',
         PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/<title>/update/',
         PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/<title>/delete/',
         PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/<title>/<int:fk>/',
         PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('comments/<int:pk>/delete/',
         CommentDeleteView.as_view(template_name='blog/comment_confirm_delete.html'),
         name='comment-delete'),
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
]
