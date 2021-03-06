import django
from django.db import models

# Create your models here.
class Family(models.Model):
    class Meta:
        db_table = 'family'

    family_name_en = django.db.models.CharField(verbose_name = '苗字(英)', max_length=20)
    family_name_jp = django.db.models.CharField(verbose_name = '苗字(日)', max_length=20)
    boss_id = django.db.models.IntegerField(verbose_name = '代表者ID')
    disp_flg = django.db.models.BooleanField(verbose_name = '表示フラグ')
    create_date = django.db.models.DateTimeField(verbose_name = '作成日', auto_now_add = True)
    update_date = django.db.models.DateTimeField(verbose_name = '更新日', auto_now = True)
    del_flg = django.db.models.BooleanField(verbose_name = '削除フラグ')

    def __str__(self):
        return self.family_name_jp#Todo 何を返すべきか

class Member(models.Model):
    class Meta:
        db_table = 'member'

    login_id = django.db.models.CharField(verbose_name = 'ログインID', max_length=20,null=False)
    password = django.db.models.CharField(verbose_name = 'パスワード', max_length=20,null=False)
    family_id = django.db.models.IntegerField(verbose_name = '家族ID')
    first_name_en = django.db.models.CharField(verbose_name = '名前(英)', max_length=20)
    first_name_jp = django.db.models.CharField(verbose_name = '名前(日)', max_length=20)
    birth_day = django.db.models.DateTimeField(verbose_name = '誕生日')
    session_id = django.db.models.CharField(verbose_name = 'セッションID',max_length=50,null=True)
    disp_flg = django.db.models.BooleanField(verbose_name = '表示フラグ')
    create_date = django.db.models.DateTimeField(verbose_name = '作成日', auto_now_add = True)
    update_date = django.db.models.DateTimeField(verbose_name = '更新日', auto_now = True)
    del_flg = django.db.models.BooleanField(verbose_name = '削除フラグ')

    def __str__(self):
        return self.password#Todo 何を返すべきか,passwordはなし
