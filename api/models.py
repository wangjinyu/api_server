from django.db import models
from django.contrib.auth.models import AbstractUser

class UserInfo(AbstractUser):
    int_id = models.CharField(blank=True, max_length=8, default='')
    age  = models.IntegerField(blank=True, null=True)
    class Meta:
        db_table = 'user_info'
        verbose_name = 'user_info'
        verbose_name_plural = '用户信息'
