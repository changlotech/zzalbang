from django.contrib.auth.models import User
from django.db import models

class Gallery(models.Model):
    #갤러리 썸네일
    image = models.ImageField(upload_to='gallery/', null=False)
    #갤러리 이름
    title = models.CharField(max_length=20, null=False)
    #갤러리 설명
    description = models.CharField(max_length=200, null=False)
    #갤러리 생성날짜
    created_at = models.DateTimeField(auto_now_add=True)
    #작성자
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
