from django.urls import path
from . import views

app_name = "accountapp"

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('create/', views.AccountCreateView.as_view(), name='create'),
]