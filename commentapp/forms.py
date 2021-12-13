from django.forms import ModelForm

from commentapp.models import Comment


class CommentCreationForm(ModelForm):
    class Meta:
        #어떤 모델을 쓸 것인가
        model = Comment
        #Comment 모델의 어떤 필드를 html 입력폼으로 출력되게 할 것인가
        fields = ['content']