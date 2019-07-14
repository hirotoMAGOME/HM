import django
from django.db import models


# Create your models here.
#設定値モデル
class UserAdminConfig(models.Model):
    class Meta:
        db_table = 'user_admin_config'

    name = django.db.models.CharField(verbose_name='設定値名', max_length=20, null=False)
    memo = django.db.models.CharField(verbose_name='設定値メモ', max_length=100, null=True)
    value = django.db.models.CharField(verbose_name='設定値メモ', max_length=100, null=True)
    rank = django.db.models.IntegerField(verbose_name='表示順', null=True)

    def __str__(self):
        return self.name
