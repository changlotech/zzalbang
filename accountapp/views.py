from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorator import account_ownership_required
from accountapp.forms import AccountUpdateForm
from articleapp.models import Article

has_ownership = [account_ownership_required, login_required]

def hello_world(request):
    return render(request, 'accountapp/hello.html')

class AccountCreateView(CreateView):
    #유저라는 모델로 CreatView를 만들것이다.
    model = User
    #User 모델을 만들기위한 폼은 UserCreationForm을 이용할 것이다.
    form_class = UserCreationForm
    #계정생성을 성공하면 리다이렉트할 위치
    success_url = reverse_lazy('accountapp:hello_world')
    #UserCreationForm을 찍어낼 template 즉 html은 무엇을 사용할 것인가
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView,MultipleObjectMixin):
    #어떤 모델을 쓸건지
    model = User
    #어떤 템플릿에서 시각화해서 보여줄 것인지
    template_name = 'accountapp/detail.html'
    #위의 템플릿에서 User 모델을 어떤 변수명으로 사용할 것인지
    context_object_name = 'target_user'

    paginate_by = 12

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)

#method_decorator라는 번역기를 달아서, 클래스 안의 메소드에도 작용하도록
# import를 has_ownership으로 묶어 주고, 두 줄로 줄임
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    #어떤 모델을 쓸건지
    model = User
    #User 모델의 정보를 수정하기 위한 폼은 AccoutUpdateForm으로 할 것이다.
    form_class = AccountUpdateForm
    #계정정보 수정을 성공하면 리다이렉트 위치를 정해준다
    success_url = reverse_lazy('accountapp:hello_world')
    #정보수정을 할 때 html은 어떤 template html을 쓸 것인지
    template_name = 'accountapp/update.html'
    #위의 html에서 User모델을 어떤 변수로 화면출력이 되게 할 것인가
    context_object_name = 'target_user'

    #겟요청 처리 겟 메소드 오버라이딩

#method_decorator라는 번역기를 달아서, 클래스 안의 메소드에도 작용하도록
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    #어떤 모델을 쓸건지
    model = User
    #회원 탈퇴가 성공하면 어디로 리다이렉트 할 것인지
    Success_url = reverse_lazy('accountapp:login')
    #회원탈퇴 할 때 쓸 html은 어떤 template html 이용할 것인지
    template_name = 'accountapp/delete.html'
    #위의 템플릿에서 User모델을 어떤 변수명으로 사용할 것인지
    context_object_name = 'target_user'

    # 겟요청 처리 겟 메소드 오버라이딩
    #지우고 데코레이션 함수 로 대체




