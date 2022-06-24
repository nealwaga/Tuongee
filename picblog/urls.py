from django import views
from django.urls import path
#from . import views
from . views import CelebrityView, DoctorView, HomeView, PostDetailView, CreatePostView, DeletePostView, CreateCommentView, UpdatePostView

urlpatterns = [
    
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>',PostDetailView.as_view(),name="post"),
    path('create_post/', CreatePostView.as_view(),name="create"),
    path('article/<int:pk>/delete_post',DeletePostView.as_view(), name="delete"),
    path('article/<int:pk>/comment', CreateCommentView.as_view(),name="comment"),
    path('doctors/',DoctorView.as_view(),name="doctors"),
    path('celebrities/',CelebrityView.as_view(),name="celebrities"),
    path('article/edit/<int:pk>',UpdatePostView.as_view(), name='update')
]