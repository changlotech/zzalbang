from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView

from galleryapp.forms import GalleryCreationForm
from galleryapp.models import Gallery

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class GalleryCreateView(CreateView):
    #모델은 갤러리
    model = Gallery
    #갤리리 모델로 부터 Gallery 인스턴스를 생성하기위해 사용할 Form은 GalleryCreationForm이다
    form_class = GalleryCreationForm
    #위 GalleryCreationForm을 찍어낼 html은 galleryapp의 create.html 이다.
    template_name = 'galleryapp/create.html'

  #over-riding 방법
    def form_valid(self, form):
        temp_gallery = form.save(commit=False)
        temp_gallery.writer = self.request.user
        temp_gallery.save()
        return super().form_valid(form)

    #Gallery 인스턴스객체가 성공적으로 생성이되면 이동할 html
    #GalleryCreationForm 으로 막 생성한 특정갤러리의 디테일 페이지로 이동
    def get_success_url(self):
        return reverse('galleryapp:detail', kwargs={'pk': self.object.pk})

class GalleryDetailView(DetailView):
    model = Gallery
    template_name = 'galleryapp/detail.html'
    context_object_name = 'target_gallery'
