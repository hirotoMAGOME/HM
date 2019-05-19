from django import forms
from . import models

PLUS_FLG_CHOICES = (
    ('1', '収入'),
    ('0', '支出'),
)


#class PaymentPlanForm(forms.Form):



class PaymentResultForm(forms.Form):
    #予算情報
    name_plan = forms.ModelChoiceField(models.PaymentPlan.objects, label='予算')
    amount_plan = forms.CharField(label='金額')
    payment_limit = forms.ModelChoiceField(models.PaymentPlan.objects, label='締め日')

    #実績情報
    #TODO プルダウンやめる。ダイナミックサーチ
    name = forms.ModelChoiceField(
        models.PaymentResult.objects,
        label='予算',
    )
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
    payment_date = forms.DateTimeField(
        label='支払日',
        required=True,
        widget=forms.DateInput(attrs={"type": "date"}),
        input_formats=['%Y-%m-%d'],
    )
