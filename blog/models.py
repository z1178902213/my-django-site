from django.db import models

# Create your models here.
class User(models.Model):
    # verbose_name为显示的名称，如果可以为空设置blank=True，需要默认值则设置default='默认值'
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=8, verbose_name='用户名')
    gender = models.CharField(max_length=1, verbose_name='性别')
