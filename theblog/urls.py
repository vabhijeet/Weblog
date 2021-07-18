
from django.urls import path
from django.views.generic.list import ListView
from .views import HomeView,ArticleDetailView,AddPostView,UpdatePostView,CategoryView,DeletePostView,AddCategoryView,LikeView,AddCommentView;



urlpatterns = [ 
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('add-category/', AddCategoryView.as_view(), name='add-category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name='delete-post'),
    path('category/<str:cats>',CategoryView,name='category'),
    path('like/<int:pk>', LikeView, name='like-post'),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name='add-comment'),
]
