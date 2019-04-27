from django.shortcuts import render, redirect
from django.views import View

from budget.forms import PaymentPlanForm

from budget.models import PaymentPlan, PaymentResult, PaymentUnit, PaymentCategory, WalletType, Wallet


class IndexView(View):
    def get(self, request, *args, **kwargs):
        """GET リクエスト用のメソッド"""

        payment_result_data = PaymentResult.objects.select_related('payment_plan').all()

        context = {
            'data': payment_result_data,
            'form': PaymentPlanForm()
        }
        print(payment_result_data)

        return render(request, 'budget/index.html', context)

    def post(self, request, *args, **kwargs):
        """POST リクエスト用のメソッド"""


index = IndexView.as_view()