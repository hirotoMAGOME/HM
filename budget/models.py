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
    del_flg = django.db.models.BooleanField(verbose_name='削除フラグ', null=False, default=0)

    def __str__(self):
        return self.name


class WalletHistory(models.Model):
    class Meta:
        db_table = 'wallet_history'

    wallet_id = django.db.models.ForeignKey(Wallet, on_delete=models.PROTECT, null=False)
    balance = django.db.models.IntegerField(verbose_name='残高', null=False, default=0)
    family_id = django.db.models.IntegerField(verbose_name='家族ID', null=False, default=0)
    member_id = django.db.models.IntegerField(verbose_name='メンバーID', null=False, default=0)
    create_date = django.db.models.DateTimeField(verbose_name='作成日', null=False)
    update_date = django.db.models.DateTimeField(verbose_name='更新日', null=False)
    del_flg = django.db.models.BooleanField(verbose_name='削除フラグ', null=False, default=0)

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

    payment_category = django.db.models.ForeignKey(PaymentCategory, verbose_name='支払いカテゴリID', on_delete=models.PROTECT, null=True)
    name = django.db.models.CharField(verbose_name='名前', max_length=20, null=True)
    memo = django.db.models.CharField(verbose_name='備考', max_length=100, null=True)
    amount_plus_flg = django.db.models.BooleanField(verbose_name='収支区分', default=0)
    amount = django.db.models.IntegerField(verbose_name='金額', null=True)
    payment_unit = django.db.models.ForeignKey(PaymentUnit, verbose_name='支払い単位ID', on_delete=models.PROTECT, null=False, default=1)
    payment_limit = django.db.models.IntegerField(verbose_name='支払いリミット', null=True)
    rank = django.db.models.IntegerField(verbose_name='表示順', null=True)
    family_id = django.db.models.IntegerField(verbose_name='家族ID', null=True)
    member_id = django.db.models.IntegerField(verbose_name='メンバーID', null=True)
    """nullの削除"""
    create_date = django.db.models.DateTimeField(verbose_name='作成日', auto_now_add=True, null=True)
    """nullの削除"""
    update_date = django.db.models.DateTimeField(verbose_name='更新日', auto_now=True, null=True)
    del_flg = django.db.models.BooleanField(verbose_name='削除フラグ', default=0)
        
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
    rank = django.db.models.IntegerField(verbose_name='表示順', null=True)
    payment_month = django.db.models.DateTimeField(verbose_name='支払月', null=True)
    payment_date = django.db.models.DateTimeField(verbose_name='支払日', null=True)
    sample_flg = django.db.models.BooleanField(verbose_name='サンプルフラグ', default=0)
    family_id = django.db.models.IntegerField(verbose_name='家族ID', null=True)
    member_id = django.db.models.IntegerField(verbose_name='メンバーID', null=True)
    create_date = django.db.models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    update_date = django.db.models.DateTimeField(verbose_name='更新日', auto_now=True)
    del_flg = django.db.models.BooleanField(verbose_name='削除フラグ', default=0)

    def __str__(self):
        return self.memo


class Settlement(models.Model):
    settlement_month = django.db.models.DateTimeField(verbose_name='決算月', unique_for_month=True, null=False)
    settlement_date = django.db.models.DateTimeField(verbose_name='決算日', null=False)
    family_id = django.db.models.IntegerField(verbose_name='家族ID', null=True)
    member_id = django.db.models.IntegerField(verbose_name='メンバーID', null=True)
    create_date = django.db.models.DateTimeField(verbose_name='作成日', null=False, auto_now_add=True)
    update_date = django.db.models.DateTimeField(verbose_name='更新日', null=False, auto_now=True)
    del_flg = django.db.models.BooleanField(verbose_name='削除フラグ', null=False, default=0)


class DoublePost(models.Model):
    """2重POST防止用モデル"""
    class Meta:
        db_table = 'double_post'

    csrf = django.db.models.CharField(verbose_name='csrf', max_length=100, null=False)
    post_text = django.db.models.CharField(verbose_name='POST内容', max_length=1000, null=False)
    create_date = django.db.models.DateTimeField(verbose_name='作成日', auto_now_add=False)