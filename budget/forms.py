from django import forms
from . import models

PLUS_FLG_CHOICES = (
    ('1', '収入'),
    ('0', '支出'),
)


class PaymentPlanForm(forms.Form):
    #予算情報
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
    planform_payment_unit_id = forms.IntegerField(
        label='単位'
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
