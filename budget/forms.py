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
