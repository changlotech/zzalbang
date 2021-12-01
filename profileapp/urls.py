from django.urls import path
from . import views

app_name= 'profileapp'


#views의 함수와 url들 연결
urlpatterns = [
    path('create/', views.ProfileCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.ProfileUpdateView.as_view(), name='update'),
]