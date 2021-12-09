from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'articleapp'

urlpatterns = [
     path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'),
     path('create/', views.ArticleCreateView.as_view(), name='create'),
     path('detail/<int:pk>/', views.ArticleDetailView.as_view(), name='detail'),
     path('update/<int:pk>/', views.ArticleUpdateView.as_view(), name='update'),
     path('', TemplateView.as_view(template_name='articleapp/list.html'), name='list'),
     path('delete/<int:pk>/', views.ArticleDeleteView.as_view(), name='delete'),

]