from . import views
from django.urls import path

app_name = 'likeapp'

urlpatterns = [
    path('article/like/<int:pk>/', views.LikeArticleView.as_view(), name='article_like')

]
