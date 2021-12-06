from django.contrib.auth.models import User
from django.db import models

class Article(models.Model):
    #유저객체와 포린키로 연결, 유저가 탈퇴해도 게시글은 사라지지 않는다
    #유저객체에서 Article객체에 접근할 때 쓸 이름은 article, set_NULL으로 한다고 했으니 당연히 null=True 입력해줘야함
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='ariticle', null=True)
    title = models.CharField(max_length=200)
    #저장위지 반드시 저장
    image = models.ImageField(upload_to='article/', null=False)
    #내용작성 필드
    content = models.TextField()
    #작성날짜, add로 게시글 생성했을 때의 시간으로 저장됨.
    created_at = models.DateTimeField(auto_now_add=True)


