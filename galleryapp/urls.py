from django.urls import path
from . import views

app_name = 'galleryapp'

urlpatterns = [
    path('create/', views.GalleryCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.GalleryDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.GalleryUpdateView.as_view(), name='update'),
    path('list/', views.GalleryListView.as_view(), name='list'),

]
