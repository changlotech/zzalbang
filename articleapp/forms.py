from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
      #Meta정보를 활용할 때 Meta클래스 안에서 작성
    class Meta:
        #Article 모델을 이용해서 html 입력 Form 만들 것임
        model = Article
        # html 입력폼에서 사용자(user)로 부터 title, image, conten를 입력한다.  이 모든 것이 장고가 db에 저장
        fields = ['title', 'image', 'content', 'gallery']
