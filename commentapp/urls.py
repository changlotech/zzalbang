from django.urls import path
#url.py 와 views.py의 함수를 가져오기 위해
from . import views

app_name='commentapp'

urlpatterns =[
    path('create/', views.CommentCreateView.as_view(), name='create'),


]