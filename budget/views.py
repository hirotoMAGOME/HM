from django.shortcuts import render, redirect
from django.views import View

from budget.forms import PaymentPlanForm

from budget.models import PaymentPlan, PaymentResult, PaymentUnit, PaymentCategory, WalletType, Wallet


class IndexView(View):
    def get(self, request, *args, **kwargs):
        """GET リクエスト用のメソッド"""

        payment_unit = PaymentUnit.objects.values('id', 'name_en')


        #TODO unit_idを固定値ではなくroopで回す
        #######################################################################################################################
        #どっちが早いか、あとで検証
        payment_result_data = PaymentResult.objects.select_related('payment_plan').all()
        payment_result_data1 = payment_result_data.filter(payment_plan__payment_unit_id=1)
        payment_result_data2 = payment_result_data.filter(payment_plan__payment_unit_id=2)
        payment_result_data3 = payment_result_data.filter(payment_plan__payment_unit_id=3)
        payment_result_data4 = payment_result_data.filter(payment_plan__payment_unit_id=4)
        payment_result_data5 = payment_result_data.filter(payment_plan__payment_unit_id=5)

        #payment_result_data1 = PaymentResult.objects.select_related('payment_plan').filter(payment_plan__payment_unit_id=1)
        #payment_result_data2 = PaymentResult.objects.select_related('payment_plan').filter(payment_plan__payment_unit_id=2)
        #payment_result_data3 = PaymentResult.objects.select_related('payment_plan').filter(payment_plan__payment_unit_id=3)
        #payment_result_data4 = PaymentResult.objects.select_related('payment_plan').filter(payment_plan__payment_unit_id=4)
        #payment_result_data5 = PaymentResult.objects.select_related('payment_plan').filter(payment_plan__payment_unit_id=5)

        #######################################################################################################################

        context = {
            'data1': payment_result_data1,
            'data2': payment_result_data2,
            'data3': payment_result_data3,
            'data4': payment_result_data4,
            'data5': payment_result_data5,
            'unit_data':payment_unit,
            'form': PaymentPlanForm()
        }

        return render(request, 'budget/index.html', context)

    def post(self, request, *args, **kwargs):
        """POST リクエスト用のメソッド"""


index = IndexView.as_view()