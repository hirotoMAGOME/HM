import django
from django.db import models


# Create your models here.
class Wallet(models.Model):
    class Meta:
        db_table = 'wallet'

    name = django.db.models.CharField(verbose_name='名前', max_length=20)
    wallet_type_id = django.db.models.IntegerField(verbose_name='財布種別ID')
    balance = django.db.models.IntegerField(verbose_name='残高')
    rank = django.db.models.IntegerField(verbose_name='表示順', null=True)
    family_id = django.db.models.IntegerField(verbose_name='家族ID', null=True)
    member_id = django.db.models.IntegerField(verbose_name='メンバーID', null=True)
    create_date = django.db.models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    update_date = django.db.models.DateTimeField(verbose_name='更新日', auto_now=True)
    del_flg = django.db.models.BooleanField(verbose_name='削除フラグ', default=0)

    def __str__(self):
        return self.name


class WalletType(models.Model):
    class Meta:
        db_table = 'wallet_type'

    name = django.db.models.CharField(verbose_name='名前', max_length=20)
    family_id = django.db.models.IntegerField(verbose_name='家族ID', null=True)
    member_id = django.db.models.IntegerField(verbose_name='メンバーID', null=True)

    def __str__(self):
        return self.name


class PaymentCategory(models.Model):
    class Meta:
        db_table = 'payment_category'

    name = django.db.models.CharField(verbose_name='名前', max_length=20)
    sample = django.db.models.CharField(verbose_name='例', max_length=100, null=True)
    memo = django.db.models.CharField(verbose_name='備考', max_length=100, null=True)
    family_id = django.db.models.IntegerField(verbose_name='家族ID', null=True)
    member_id = django.db.models.IntegerField(verbose_name='メンバーID', null=True)

    def __str__(self):
        return self.name


class PaymentUnit(models.Model):
    class Meta:
        db_table = 'payment_unit'

    #1,2,3,4,5 不定期、年、月、週、日
    name = django.db.models.CharField(verbose_name='名前', max_length=20, null=False, default='nothing')
    name_en = django.db.models.CharField(verbose_name='名前(英)', max_length=20, null=False, default='nothing')

    def __str__(self):
        return self.name


class PaymentPlan(models.Model):
    """予算モデル"""
    class Meta:
        db_table = 'payment_plan'

    payment_category_id = django.db.models.IntegerField(verbose_name='支払いカテゴリID', null=True)
    name = django.db.models.CharField(verbose_name='名前', max_length=20, null=True)
    memo = django.db.models.CharField(verbose_name='備考', max_length=100, null=True)
    amount_plus_flg = django.db.models.BooleanField(verbose_name='収支区分', default=0)
    amount = django.db.models.IntegerField(verbose_name='金額', null=True)
    payment_unit = django.db.models.ForeignKey(PaymentUnit, verbose_name='支払い単位ID', on_delete=models.PROTECT, null=False, default=1)
    payment_limit = django.db.models.IntegerField(verbose_name='支払いリミット', null=True)
    rank = django.db.models.IntegerField(verbose_name='表示順', null=True)
    family_id = django.db.models.IntegerField(verbose_name='家族ID', null=True)
    member_id = django.db.models.IntegerField(verbose_name='メンバーID', null=True)
        
    def __str__(self):
        return self.name


class PaymentResult(models.Model):
    """実収支モデル"""
    class Meta:
        db_table = 'payment_result'

    payment_plan = django.db.models.ForeignKey(PaymentPlan, verbose_name='予算', on_delete=models.PROTECT, null=False)
    amount_plus_flg = django.db.models.BooleanField(verbose_name='収支区分', default=0)
    amount = django.db.models.IntegerField(verbose_name='金額', null=True)
    memo = django.db.models.CharField(verbose_name='備考', max_length=100, null=True)
    family_id = django.db.models.IntegerField(verbose_name='家族ID', null=True)
    member_id = django.db.models.IntegerField(verbose_name='メンバーID', null=True)
    rank = django.db.models.IntegerField(verbose_name='表示順', null=True)
    payment_date = django.db.models.DateTimeField(verbose_name='支払日')
    create_date = django.db.models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    update_date = django.db.models.DateTimeField(verbose_name='更新日', auto_now=True)
    del_flg = django.db.models.BooleanField(verbose_name='削除フラグ', default=0)

    def __str__(self):
        return self.memo
