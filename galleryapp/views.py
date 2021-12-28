from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from galleryapp.decorators import gallery_ownership_required
from galleryapp.forms import GalleryCreationForm
from galleryapp.models import Gallery
from subscribeapp.models import Subscription


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

#MultipleObjectMixin은 여러가지 object들을 다룰 수 있게 만들어 주는 클래스
class GalleryDetailView(DetailView, MultipleObjectMixin):
    model = Gallery
    template_name = 'galleryapp/detail.html'
    context_object_name = 'target_gallery'
    #
    paginate_by = 20
    # 아래 겟컨텍스트  는 템플릿으로 무언가(인스턴스)를 출력하고 싶을 때 쓰는 메소드
    def get_context_data(self, **kwargs):
        #특정 pk 값을 갖는 갤러리 한개를 gallery변수에 담는다
        gallery = self.object
        #구독버튼을 누른 유저를 user변수에 담는다.
        user = self.request.user
        #유저가 인증된 유저라면 즉 로그인 했다면
        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, gallery=gallery)
        else:
            subscription = None

        #get_object()는 특정 pk값을 갖는 object를 가져오는 메소드. 여기서는 Gallery 한개.
        #Article객체를 필터링 한다. gallery 필드가 특정 Gallery로 채워진 Article들로
        object_list = Article.objects.filter(gallery=self.get_object()).order_by('-pk')
        return super(GalleryDetailView, self).get_context_data(object_list=object_list, subscription=subscription,  **kwargs)


@method_decorator(gallery_ownership_required, 'get')
@method_decorator(gallery_ownership_required, 'post')
class GalleryUpdateView(UpdateView):
    #모델
    model = Gallery
    #사용자 입력 폼
    form_class = GalleryCreationForm
    #html
    template_name = 'galleryapp/update.html'
    #인스턴스
    context_object_name = 'target_gallery'


    #성공하면

    def get_success_url(self):
        return reverse('galleryapp:detail', kwargs={'pk': self.object.pk})

 #galery_list.html이 디폴트 이지만, 우리가 새 이름 지정
class GalleryListView(ListView):
    #어떤 모델 쓸것인가
    model = Gallery
    #갤러리 리스트 뭉탱이를 찍어내는 html은 어떤 html을 쓸 것인가?
    template_name = 'galleryapp/List.html'
    #위의 html에서 어떤이름으로 갤러리 리스트 뭉탱이를 표현할 것인가
    context_object_name = 'gallery_list'
    #갤러리를 몇개식 만들기
    paginate_by = 15

