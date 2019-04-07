import django
from django.db import models

# Create your models here.
class Wallet(models.Model):
    class Meta:
        db_table = 'wallet'

    name = django.db.models.CharField(verbose_name = '名前', max_length=20)
    wallet_type_id = django.db.models.IntegerField(verbose_name = '財布種別ID')
    balance = django.db.models.IntegerField(verbose_name = '残高')
    family_id = django.db.models.IntegerField(verbose_name='家族ID',null=True)
    member_id = django.db.models.IntegerField(verbose_name='メンバーID',null=True)
    create_date = django.db.models.DateTimeField(verbose_name = '作成日', auto_now_add = True)
    update_date = django.db.models.DateTimeField(verbose_name = '更新日', auto_now = True)
    del_flg = django.db.models.BooleanField(verbose_name = '削除フラグ',default=0)

    def __str__(self):
        return self.name

class WalletType(models.Model):
    class Meta:
        db_table = 'wallet_type'

    name = django.db.models.CharField(verbose_name = '名前', max_length=20)
    family_id = django.db.models.IntegerField(verbose_name='家族ID',null=True)
    member_id = django.db.models.IntegerField(verbose_name='メンバーID',null=True)

    def __str__(self):
        return self.name


class Payment(models.Model):
    class Meta:
        db_table = 'payment'

    payment_category_id = django.db.models.IntegerField(verbose_name='支払いカテゴリID')
    name = django.db.models.CharField(verbose_name='名前', max_length=20)
    memo = django.db.models.CharField(verbose_name='備考', max_length=100,null=True)
    amount = django.db.models.IntegerField(verbose_name='金額')
    payment_unit_id = django.db.models.IntegerField(verbose_name='支払い単位ID',null=True)
    payment_limit = django.db.models.IntegerField(verbose_name='支払いリミット',null=True)
    family_id = django.db.models.IntegerField(verbose_name='家族ID',null=True)
    member_id = django.db.models.IntegerField(verbose_name='メンバーID',null=True)
    rank = django.db.models.IntegerField(verbose_name='表示順',null=True)
        
    def __str__(self):
        return self.name

class PaymentCategory(models.Model):
    class Meta:
        db_table = 'payment_category'

    name = django.db.models.CharField(verbose_name = '名前', max_length=20)
    sample = django.db.models.CharField(verbose_name='例', max_length=100,null=True)
    memo = django.db.models.CharField(verbose_name='備考', max_length=100,null=True)
    family_id = django.db.models.IntegerField(verbose_name='家族ID',null=True)
    member_id = django.db.models.IntegerField(verbose_name='メンバーID',null=True)

    def __str__(self):
        return self.name

class PaymentUnit(models.Model):
    class Meta:
        db_table = 'payment_unit'

    #1,2,3,4,5 回、年、月、週、日
    name = django.db.models.CharField(verbose_name = '名前', max_length=20)

    def __str__(self):
        return self.name