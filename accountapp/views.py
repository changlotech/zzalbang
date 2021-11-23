from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


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