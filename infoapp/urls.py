from django.urls import path
from . import views

app_name = 'infoapp'

urlpatterns = [

    path('info/', views.info, name='info'),
    path('notice/', views.notice, name='notice'),
    path('contact/', views.contact, name='contact'),
    path('company/', views.company, name='company'),
]