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