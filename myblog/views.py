from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import BlogPost

# Create your views here.

def PostListView(request):
    pageTitle = 'Blog posts'
    blogPostList = BlogPost.objects.order_by('-date_posted')[:5]
    context = { 'blogPostList': blogPostList,
            'pageTitle': pageTitle,
    }
    return render(request, 'myblog/home.html', context)

def PostDetailView(request, post_id):
    pageTitle = 'Post detail'

    # get post or return 404
    blogPost = get_object_or_404(BlogPost, id=post_id)

    context = {
            'blogPost': blogPost,
            'pageTitle': pageTitle,
            }

    return render(request, 'myblog/detail.html', context)

# Takes integer for month
# return all of blog posts of published that month
def PostMonthView(request, month):
    # Reject invalid requests
    if(month>12 or month<1):
        return Http404()
    return HttpResponse("Post month view, month of: %s." % month)
    
def PostYearView(request, year):
    return HttpResponse("Post year view, year: %s." % year)
