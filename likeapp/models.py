from django.contrib.auth.models import User
from django.db import models

from articleapp.models import Article


class LikeRecord(models.Model):
    #'like'라는 인스턴스객체에 저장할 정보 1)user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_record')
    #'좋아요'라는 인스턴스객체 저장할 정보 2)article댓글pk
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='like_record')

    class Meta:
        unique_together = ('user', 'article')

