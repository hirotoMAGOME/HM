from django import forms
from . import models

class PaymentPlanForm(forms.Form):
    login_id = forms.CharField(
        label='ユーザー名',
        max_length=20,
    )

    password = forms.CharField(
        label = 'パスワード',
        strip=False,
        widget=forms.PasswordInput(render_value=True),
    )

    family = forms.ModelChoiceField(models.Family.objects,label='家族名')

    name = forms.CharField(models.PaymentPlan.objects,label='収支予定名')
    amount = forms.IntegerField(models.PaymentPlan.objects,label='金額')
    payment_unit_id = forms.IntegerField(verbose_name='支払い単位ID',null=True)
    payment_limit = forms.IntegerField(verbose_name='支払いリミット',null=True)