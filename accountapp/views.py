from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm


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


class AccountDetailView(DetailView):
    #어떤 모델을 쓸건지
    model = User
    #어떤 템플릿에서 시각화해서 보여줄 것인지
    template_name = 'accountapp/detail.html'
    #위의 템플릿에서 User 모델을 어떤 변수명으로 사용할 것인지
    context_object_name = 'target_user'



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

class AccountDeleteView(DeleteView):
    #어떤 모델을 쓸건지
    model = User
    #회원 탈퇴가 성공하면 어디로 리다이렉트 할 것인지
    Success_url = reverse_lazy('accountapp:login')
    #회원탈퇴 할 때 쓸 html은 어떤 template html 이용할 것인지
    template_name = 'accountapp/delete.html'
    #위의 템플릿에서 User모델을 어떤 변수명으로 사용할 것인지
    context_object_name = 'target_user'