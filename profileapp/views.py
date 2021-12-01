from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorator import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    #어떤 모델을 쓸것인가
    model = Profile
    #Profile 모델을 만들기 위한 폼은 ProfileCreationForm 이라는 것을 쓸것이다
    form_class =  ProfileCreationForm
    #프로필 생성을 성공하면 어디로 리다이렉트 되게 할 것인가
    success_url = reverse_lazy('accountapp:hello_world')
    #ProfileCreationForm 찍어낼 template은 무슨 html을 쓸 것인가?
    template_name = 'profileapp/create.html'

    #유저ID를 자동입력시키기 위해 오버라이드
    def form_valid(self, form):
        #DB에 저장하기 전에 잠깐 멈출
        temp_profile = form.save(commit=False)
        #Profile 객체의 user필드를 자동저작
        temp_profile.user = self.request.user
        temp_profile.save()
        #자바의 @오버라이드 대신하는 줄
        return super().form_valid(form)

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    # 어떤 모델을 쓸 것인가.
    model = Profile
    # Profile 모델을 수정하기 위한 폼은 ProfileCreationForm이용할 것이다.
    form_class = ProfileCreationForm
    # Profile 정보를 수정을 성공하면 리다이렉트할 위치
    success_url = reverse_lazy('accountapp:hello_world')
    #Profile 정보를 수정할 때 쓸 html은 어떤 template html쓸 것인가
    template_name = 'profileapp/update.html'
    # Profile 객체를 html(템플릿파일)에서 찍어낼 때 어떤 변수로 찍어낼 것인가
    context_object_name = 'target_profile'