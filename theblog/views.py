from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import generic
from .models import Category, Post
from .forms import PostForm,UpdateForm

class HomeView(generic.ListView):
    model=Post
    template_name= 'home.html'
    ordering=['-post_date']

class ArticleDetailView(generic.DetailView):
    model=Post
    template_name= 'article.html'
    
class AddPostView(generic.CreateView):
    model=Post
    form_class= PostForm
    template_name= 'add-post.html'

class AddCategoryView(generic.CreateView):
    model=Category
    fields='__all__'
    #form_class= PostForm
    template_name= 'add-category.html'    

class UpdatePostView(generic.UpdateView):
    model=Post
    form_class= UpdateForm
    #fields=['title', 'title_tag', 'body']
    template_name= 'update_post.html'    
    #fields='__all__'

class DeletePostView(generic.DeleteView):
    model=Post
    template_name= 'delete_post.html'
    success_url=reverse_lazy('home')
    #form_class= UpdateForm
    #fields=['title', 'title_tag', 'body']
            
# def home(request):
#     return render(request,'home.html',{})

# Create your views here.
