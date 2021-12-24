from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
      #Meta정보를 활용할 때 Meta클래스 안에서 작성
    class Meta:
        #Article 모델을 이용해서 html 입력 Form 만들 것임
        model = Article
        # html 입력폼에서 사용자(user)로 부터 title, image, conten를 입력한다.  이 모든 것이 장고가 db에 저장
        fields = ['title', 'image', 'content']

        #서머노트 .   widget 속성으로 만들어질 폼에 스타일등을 정해줄 수 있다.
        widgets = {
            'content': SummernoteWidget()
        }

        # lables 속성으로 html에서 나타나는 필드 입력폼칸의 이름을 바꿔 줄 수 있다.
        labels = {
            'title': '제목',
            'image': '사진',
            'content': '내용'
       }