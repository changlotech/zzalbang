

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from galleryapp.models import Gallery
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        # GET 방식으로 보낸 요청중에서 gallery_pk 의 값을 얻어서 galleryapp:detail 에 뿌려줌 즉 구독한 그 갤러리 디테일페이지로 리다이렉트
        return reverse('galleryapp:detail', kwargs={'pk': self.request.GET.get('gallery_pk')})

    # get 오버라이딩
    # Subscription 객체는 어떤 Gallery 에 대한 구독인지, 그리고 그 Gallery 에 대해 구독을 요청한 User 에 대한 정보를 담고있다.
    def get(self, request, *args, **kwargs):
        gallery = get_object_or_404(Gallery, pk=self.request.GET.get('gallery_pk'))
        user = self.request.user
        # 특정 Gallery 에 대해서 특정 User 가 구독을 함. 그것을 subscription 변수에 담는다.
        subscription = Subscription.objects.filter(user=user, gallery=gallery)

        # 구독정보가 존재한다면 (구독중인상태)
        if subscription.exists():
            # 구독취소
            subscription.delete()
        # 그 반대. 즉 구독한 상태가 아니라면
        else:
            # 구독객체 생성
            Subscription(user=user, gallery=gallery).save()
        return super(SubscriptionView, self).get(request, *args, **kwargs)



@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    #모델은 Subscription
    model = Subscription
    template_name = 'subscribeapp/list.html'
    context_object_name = 'subscription_list'
    paginate_by = 30


