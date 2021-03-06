from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView

from articleapp.models import Article
from commentapp.decorators import comment_ownership_required
from commentapp.forms import CommentCreationForm, SubCommentCreationForm
from commentapp.models import Comment, SubComment


class CommentCreateView(CreateView):

    model = Comment

    form_class =  CommentCreationForm

    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        #이 함수에 덮어쓰기 오버라이딩
        #위의 html에서 사용자가 post요청을 보내 DB에 Comment객체를 만들기 직전에 잠깐 멈춤!
        temp_comment = form.save(commit=False)
        #인풋타입 히든에서 article의 pk값을 value에 담아서 article 필드를 채운다
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        #Comment 객체의 writer 필드에는 POST요청을 보낸 유저로 저장
        temp_comment.writer = self.request.user
        temp_comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        #아래object는 Comment이고   그 models.py의 article의 특정 pk값으로 가져온다. 그 pk아티클의 디테일 페이지로 간다
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})


@method_decorator(comment_ownership_required, 'post')
@method_decorator(comment_ownership_required, 'get')
class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/update.html'
    context_object_name = 'target_comment'

    #redirect page
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})


@method_decorator(comment_ownership_required, 'post')
@method_decorator(comment_ownership_required, 'get')
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'commentapp/delete.html'
    context_object_name = 'target_comment'

    # redirect page
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})



class SubCommentCreateView(CreateView):

    model = SubComment
    #SubComment 모델 인스턴스를 만들기 위해서 사용자로부터 입력받는 폼은 어떤 것을 쓸것인가
    form_class = SubCommentCreationForm
    #어떤 html에서 이 form이 출력되게 할 것인가.  댓글디테일
    template_name = 'commentapp/detail.html'

    #유효성 검사 메소드인 form_valid를 오버라이딩
    def form_valid(self, form):

        temp_subcomment = form.save(commit=False)

        temp_subcomment.comment = Comment.objects.get(pk=self.request.POST['comment_pk'])
        temp_subcomment.writer = self.request.user
        temp_subcomment.save()
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.comment.article.pk})
