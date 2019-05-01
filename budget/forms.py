from django import forms
from . import models

PLUS_FLG_CHOICES = (
    ('1', '収入'),
    ('0', '支出'),
)


class PaymentPlanForm(forms.Form):

    #TODO セレクトボックスをやめる。
    #TODO labelを直す
    name = forms.ModelChoiceField(models.PaymentPlan.objects, label='家族名')
    amount = forms.ModelChoiceField(models.PaymentPlan.objects, label='家族名')
    payment_limit = forms.ModelChoiceField(models.PaymentPlan.objects, label='家族名')
    #payment_unit = forms.ModelChoiceField(models.PaymentUnit.objects, label='家族名')


class PaymentResultForm(forms.Form):
    name = forms.ModelChoiceField(
        models.PaymentPlan.objects,
        label='予算',
    )
    amount_plus_flg = forms.ChoiceField(
        choices=PLUS_FLG_CHOICES,
        required=True,
    )
    amount = forms.CharField(
        label='金額',
    )
    memo = forms.CharField(
        label='備考',
        max_length=100,
    )
    payment_date = forms.DateTimeField(
        label='支払日',
        required=True,
        widget=forms.DateInput(attrs={"type": "date"}),
        input_formats=['%Y-%m-%d'],
    )
