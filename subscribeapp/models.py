#각 app 만들 때, 모델, 뷰, url, form, html순으로 만든다

from django.contrib.auth.models import User
from django.db import models

from galleryapp.models import Gallery


class Subscription(models.Model):
    #갤러리에 누가 구독 눌렀는지
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')
    #그 '누구'에 해당하는 사람이 어느 갤러리 구독 눌럿는지
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='subscription')

    class Meta:
        unique_together = ('user', 'gallery')
