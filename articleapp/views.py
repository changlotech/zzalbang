from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from articleapp.decorators import account_ownership_required
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    # 모델은 Article을 쓸 것이다
    model = Article
    # 입력폼은 ArticleCreationForm을 이용할 것이다
    form_class = ArticleCreationForm
    #ArticleCreationForm을 찍어낼  html은 articleapp 안의 create.html
    template_name = 'articleapp/create.html'

    #유효성 검사 메소드 form_valid를 오버라이딩

    def form_valid(self, form):
        # Article 객체를 저장하기전에 잠깐 멈춤!
        temp_article = form.save(commit=False)
        # Artcle 객체의 writer필드를 채우기
        temp_article.writer = self.request.user
        # 원래 제공 함수의 self.object = form.save() 대신에
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})

class ArticleDetailView(DetailView):
    #어떤 모델을 쓸 것인가
    model = Article
    #이 위의 특정 Ariticel 객체를 찍어내는 html은 어떤 html을 쓸 것인가
    template_name = 'articleapp/detail.html'
    # {{모델명_detail}}안쓰고, 위의 html 에서 특정 Article 객체를 어떤 으름으로 {{}}안쪽 써서 표현할 것인가
    context_object_name = 'target_article'

@method_decorator(account_ownership_required, 'get')
@method_decorator(account_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    #모델은 Article을 쓸 것인가
    model = Article
    #Article 수정할 때 입력받은 폼은 ArticleCreationForm 을 쓸 것이다
    form_class = ArticleCreationForm
    # ArticleCreationForm을 찍어낼 html은 articleapp 폴더안의 update.html
    template_name = 'articleapp/update.html'
    context_object_name = 'target_article'

    def get_success_url(self):
        # 성공 후 돌아가는 페이지
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


class ArticleDeleteView(DeleteView):
    #모델은 Article을 쓸 것이다
    model = Article
    #게시글 삭제할 버튼이 있는 html은 articleapp폴더 안의 delete.html이다
    template_name = 'articleapp/delete.html'
    #위의 html에서 특정 Article객체는 어떤 이름으로 표현할 것인가
    context_object_name = 'target_article'
    #게시글 삭제가 성공한다면 이동하게될 위치 지정
    #lazy는 딕셔너리 자료 인풋이 아닌 kwargs아닌 때
    success_url = reverse_lazy('articleapp:list')

