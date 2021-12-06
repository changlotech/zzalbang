from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

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
