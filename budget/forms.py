from django import forms
from django.db import connection
from datetime import datetime
from dateutil.relativedelta import relativedelta

PLUS_FLG_CHOICES = (
    ('1', '収入'),
    ('0', '支出'),
)

# payment_unitマスタからプルダウンを生成
cursor = connection.cursor()
cursor.execute("SELECT id,name_en FROM payment_unit")
data = cursor.fetchall()
arrUnit = list()
for i in data:
    unit = (i[0], i[1])
    arrUnit.append(unit)
PAYMENT_UNIT = arrUnit

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


class PaymentResultForm(forms.Form):
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


class DisplayForm(forms.Form):
    month = forms.ChoiceField(
        choices=DISPRAY_RANGE,
        required=True,
        initial=0,
    )