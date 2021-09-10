from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView, name='blog-home'),
    path('post/<int:post_id>/', views.PostDetailView, name='post-detail'),
    path('post/<int:month>/month/', views.PostMonthView, name='post-month'),
    path('post/<int:year>/year/', views.PostYearView, name='post-year'),
]
