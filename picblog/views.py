from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from . models import Post, Comment
from . forms import PostForm, CommentForm, UpdateForm
from django.urls import reverse_lazy



class HomeView(ListView):
    model = Post
    template_name= 'home.html'
    ordering=['-id']

class DoctorView(ListView):
    model = Post
    template_name= 'doctors.html'

class CelebrityView(ListView):
    model = Post
    template_name= 'celebrities.html'

class PostDetailView(DetailView):
    model=Post
    template_name='post.html'

class CreatePostView(CreateView):
    model=Post
    form_class=PostForm
    template_name='create.html'
    
class DeletePostView(DeleteView):
    model=Post
    template_name='delete.html'
    success_url=reverse_lazy('home')

class CreateCommentView(CreateView):
    model=Comment
    form_class=CommentForm
    template_name='comment.html'
    def form_valid(self, form):
        form.instance.post_id= self.kwargs['pk']
        return super().form_valid(form)
    
    success_url=reverse_lazy('home')


class UpdatePostView(UpdateView):
    model = Post
    form_class= UpdateForm
    template_name = 'update.html'