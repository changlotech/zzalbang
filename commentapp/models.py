from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model):
    #Article 객체랑 ForeignKey로 연결, 게시글이 삭제되어도 댓글은 DB에서 삭제 안됨, Article객체로부터 Comment객체로 접근 할 때 이름은 Cmment
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name='comment')
    #작성자
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class  SubComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True, related_name='subcomment')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='subcomment')
    #대댓글 내용
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    #자바의 toString유사, 특정객체에 유의미한 문자열 정보를 리턴하게 해준다
    def __str__(self):
        return self.content