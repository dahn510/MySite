from django.views import generic
from .models import BlogPost

# Create your views here.

class PostListView(generic.ListView):
    model = BlogPost

    pageTitle = 'Blog posts'

    context_object_name = 'blogPostList'

    ordering = ['-date_posted']

    paginate_by = 5
    
    template_name = 'myblog/home.html'

class PostDetailView(generic.DetailView):
    model = BlogPost

    pageTitle = 'Post detail'

    context_object_name = 'blogPost'

    template_name = 'myblog/detail.html'

    
