from django.shortcuts import render, redirect
from django.views import View

from budget.models import PaymentPlan, PaymentResult, PaymentUnit, PaymentCategory, WalletType, Wallet


class IndexView(View):
    def get(self, request, *args, **kwargs):
        """GET リクエスト用のメソッド"""
#        context = {
#            'form':LoginForm(),
#        }

        payment_result_data = PaymentResult.objects.all().select_related('payment_plan')

        print(vars(payment_result_data))
        return render(request, 'budget/index.html',)

    def post(self, request, *args, **kwargs):
        """POST リクエスト用のメソッド"""


index = IndexView.as_view()