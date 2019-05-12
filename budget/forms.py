from django import forms
from . import models

class PaymentPlanForm(forms.Form):

    #TODO セレクトボックスをやめる。
    #TODO labelを直す
    name = forms.ModelChoiceField(models.PaymentPlan.objects, label='家族名')
    amount = forms.ModelChoiceField(models.PaymentPlan.objects, label='家族名')
    payment_limit = forms.ModelChoiceField(models.PaymentPlan.objects, label='家族名')
    #payment_unit = forms.ModelChoiceField(models.PaymentUnit.objects, label='家族名')
