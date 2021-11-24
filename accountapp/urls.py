from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

app_name = "accountapp"

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('create/', views.AccountCreateView.as_view(), name='create'),
    path('login/', LoginView.as_view(template_name = 'accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),

]