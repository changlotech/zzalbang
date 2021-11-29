from django.contrib.auth.models import User
from django.db import models




# Create your models here.

class Profile(models. Model):
    #유저 객체랑 1:1 관계, 유저객체 삭제되면 프로필 같이 삭제, 유저객체로부터 profile로 객체접근연산자 사용가능
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    #프로필 이미지를 등록하면 그 이미지는 어디에 저장되게 할 것인가?
    image = models.ImageField(upload_to="profile/", null=True)
    #닉네임 필드 닉네임은 유일하게 할 것.
    nickname = models.CharField(max_length=20, unique=True, null=True)
    #프로필 대화명
    message = models.CharField(max_length=100, null=True)
