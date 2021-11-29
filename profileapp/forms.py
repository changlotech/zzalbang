from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        #메타정보: 파일이름, 위치경로, 생성자 정보, 필드정보, 메소드정보
        # 참고할 모델
        model = Profile
        # 어떤필드를 입력폼으로 만들것인가
        fields = ['image', 'nickname', 'message']


