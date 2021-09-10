from django.template import loader
from django.http import HttpResponse, Http404
from .models import BlogPost

# Create your views here.

def PostListView(request):
    pageTitle = 'Blog posts'
    blogPostList = BlogPost.objects.order_by('-date_posted')
    template = loader.get_template('myblog/home.html') 
    context = { 'blogPostList': blogPostList,
            'pageTitle': pageTitle,
    }
    return HttpResponse(template.render(context, request))

def PostDetailView(request):
    return HttpResponse("Post detail view, without details...")

# Takes integer for month
# return all of blog posts of published that month
def PostMonthView(request, month):
    # Reject invalid requests
    if(month>12 or month<1):
        return Http404()
    return HttpResponse("Post month view, month of: %s." % month)
    
def PostYearView(request, year):
    return HttpResponse("Post year view, year: %s." % year)
