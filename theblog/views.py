from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import generic
from .models import Category, Post
from .forms import PostForm,UpdateForm
from django.http import Http404

class HomeView(generic.ListView):
    model=Post
    template_name= 'home.html'
    ordering=['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu= Category.objects.all()
        context= super(HomeView,self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        return context

def CategoryView(request,cats):
    category_post=Post.objects.filter(category=cats.replace('-',' '))
    # try:
    #     category_post = Post.objects.get(category=cats)
    # except Post.DoesNotExist:
    #     raise Http404("Post does not exist")
    return render(request, 'categories.html', {'cats':cats.title().replace('-',' '), 'category_post':category_post});  

class ArticleDetailView(generic.DetailView):
    model=Post
    template_name= 'article.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu= Category.objects.all()
        context= super(ArticleDetailView,self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        return context
    
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
    success_message = "Updated Successfully"
    def get(self, request, *args, **kwargs):
        obj = super(DeletePostView, self).get_object()
        if not obj.author == self.request.user:
            raise Http404
        return self.post(request, *args, **kwargs)
    
    # def get(self, queryset=None):
    #     """ Hook to ensure object is owned by request.user. """
        
        


    # def get(self, request, *args, **kwargs):
    #     return self.post(request, *args, **kwargs)
    #form_class= UpdateForm
    #fields=['title', 'title_tag', 'body']
            
# def home(request):
#     return render(request,'home.html',{})

# Create your views here.
