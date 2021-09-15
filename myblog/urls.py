from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostListView, name='home'),
    path('post/<int:post_id>/', views.PostDetailView, name='post-detail'),
    path('post/<int:month>/month/', views.PostMonthView, name='post-month'),
    path('post/<int:year>/year/', views.PostYearView, name='post-year'),
]
