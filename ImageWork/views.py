from django.views.generic import ListView, CreateView
from .models import Post
from django.urls import reverse_lazy
from .forms import PostForm
from . import MineImage

class HomepageView(ListView):
    model = Post
    template_name = 'index.html'

class CreatePostView(CreateView):

    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')
