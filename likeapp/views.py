from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord


@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk': kwargs['pk']})

    def get(self, request, *args, **kwargs):

        user = self.request.user
        article = get_object_or_404(Article, pk=kwargs['pk'])

        #LikeRecord 객체가 만약 존재한다면 에러메시지를 띄운ㄷ.
        #그리고 현페이지로 리다이렉트
        if LikeRecord.objects.filter(user=user, article=article).exists():
            messages.add_message(self.request, messages.ERROR, '좋아요는 한번만 가능합니다.')
            return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk': kwargs['pk']}))
        else:
            #get요청으로 html에서 넘겨받은 2가지의 정보를 LikeRecord 인스턴스의 필드에 담아 저장
            LikeRecord(user=user, article=article).save()
        #Article 객체의 like필드에 +1을 한 값을 저장
        article.like += 1
        article.save()

        messages.add_message(self.request, messages.SUCCESS, '좋아요가 반영되었습니다.')

        return super(LikeArticleView, self).get(self.request, *args, **kwargs)