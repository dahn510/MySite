from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView, name='blog-home'),
    path('detail/', views.PostDetailView, name='post-detail'),
    path('month/<int:month>/', views.PostMonthView, name='post-month'),
    path('year/<int:year>/', views.PostYearView, name='post-year'),
]
