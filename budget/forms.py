from django import forms
from . import models

class PaymentPlanForm(forms.Form):

    name = forms.ModelChoiceField(models.PaymentPlan.objects, label='家族名')
    amount = forms.ModelChoiceField(models.PaymentPlan.objects, label='家族名')
    payment_limit = forms.ModelChoiceField(models.PaymentPlan.objects, label='家族名')
    payment_unit_id = forms.ModelChoiceField(models.PaymentPlan.objects, label='家族名')