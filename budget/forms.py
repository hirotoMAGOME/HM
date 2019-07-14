from django import forms
from django.db import connection
from datetime import datetime
from dateutil.relativedelta import relativedelta


PLUS_FLG_CHOICES = (
    ('1', '収入'),
    ('0', '支出'),
)
#walletマスタからプルダウンを生成
cursor = connection.cursor()
cursor.execute("SELECT id,name_en FROM payment_unit")
data = cursor.fetchall()
arrUnit = list()
for i in data:
    unit = (i[0], i[1])
    arrUnit.append(unit)
PAYMENT_UNIT = arrUnit



WALLET_CHOICES = (

)
# payment_unitマスタからプルダウンを生成
cursor = connection.cursor()
cursor.execute("SELECT id,name FROM wallet")
data = cursor.fetchall()
arrWallet = list()
for i in data:
    wallet = (i[0], i[1])
    arrWallet.append(wallet)
WALLET_CHOICES = arrWallet

#動的に過去3ヶ月分を作成
DISPRAY_RANGE = (
    (datetime.strftime(datetime.today(), '%-m'), datetime.strftime(datetime.today(), '%m') + '月'),
    (datetime.strftime(datetime.today() - relativedelta(months=1), '%-m'), datetime.strftime(datetime.today() - relativedelta(months=1), '%m') + '月'),
    (datetime.strftime(datetime.today() - relativedelta(months=2), '%-m'), datetime.strftime(datetime.today() - relativedelta(months=2), '%m') + '月'),
)

class PaymentPlanForm(forms.Form):
    #予算情報
    planform_id = forms.IntegerField(
        required=True,
    )
    planform_name = forms.CharField(
        label='予算名',
        required=True,
    )
    planform_payment_limit = forms.CharField(
        label='締め日',
        required=True,
    )
    planform_amount_plus_flg = forms.ChoiceField(
        choices=PLUS_FLG_CHOICES,
        required=True,
        initial=0,
    )
    planform_amount = forms.CharField(
        label='金額',
        required=True,
    )
    planform_payment_unit_id = forms.ChoiceField(
        choices=PAYMENT_UNIT,
        label='単位',
    )


class PaymentResultRegistForm(forms.Form):
    #実績情報
    #TODO プルダウンやめる。ダイナミックサーチ

    amount_plus_flg = forms.ChoiceField(
        choices=PLUS_FLG_CHOICES,
        required=True,
        initial=0,
    )
    amount = forms.CharField(
        label='金額',
        required=True,
    )
    memo = forms.CharField(
        label='備考',
        max_length=100,
    )
    payment_date = forms.DateField(
        label='支払日',
    )
    wallet = forms.ChoiceField(
        label='財布',
        choices=WALLET_CHOICES,
        required=True,
        initial=0,
    )
    selected_plan_id = forms.IntegerField(
        required=True
    )
class PaymentResultUpdateForm(forms.Form):
    #実績情報
    #TODO プルダウンやめる。ダイナミックサーチ

    PRUF_amount_plus_flg = forms.ChoiceField(
        choices=PLUS_FLG_CHOICES,
        required=True,
        initial=0,
    )
    PRUF_amount = forms.CharField(
        label='金額',
        required=True,
    )
    PRUF_memo = forms.CharField(
        label='備考',
        max_length=100,
    )
    PRUF_payment_date = forms.DateField(
        label='支払日',
    )
    PRUF_wallet = forms.ChoiceField(
        label='財布',
        choices=WALLET_CHOICES,
        required=True,
        initial=0,
    )
    PRUF_selected_result_id = forms.IntegerField(
        required=True
    )
class DisplayForm(forms.Form):
    month_select_box = forms.ChoiceField(
        choices=DISPRAY_RANGE,
        required=True,
    )


#TODO monthにplaceholderをつける
class SettlementForm(forms.Form):
    settlement_month = forms.CharField(
        label='決算月',
        required=True,
        max_length=6,
    )
    settlement_date = forms.DateField(
        label='決算日',
        required=True,
    )

    #カスタムバリデーション　フロントにエラーが戻せない
    #def clean_settlement_month(self):
    #    settlement_month = self.cleaned_data['settlement_month']
    #    if(len(settlement_month) != 6):
    #        raise forms.ValidationError("決算月はyyyymmで入力してください")
    #    return settlement_month
