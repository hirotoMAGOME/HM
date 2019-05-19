from django.shortcuts import render, redirect
from django.views import View

from budget.forms import PaymentResultForm

from budget.models import PaymentPlan, PaymentResult, PaymentUnit, PaymentCategory, WalletType, Wallet


class IndexView(View):
    def get(self, request, *args, **kwargs):
        """GET リクエスト用のメソッド"""

        #payment_unit = PaymentUnit.objects.values('id', 'name_en')

        #payment_result_data1 = PaymentResult.objects.select_related().filter(payment_plan__payment_unit_id=1).select_related().all()
        payment_result_data1 = PaymentResult.objects.select_related('payment_plan').filter(payment_plan__payment_unit_id=1).select_related('payment_plan__payment_unit').all()
        payment_result_data2 = PaymentResult.objects.select_related('payment_plan').filter(payment_plan__payment_unit_id=2).select_related('payment_plan__payment_unit').all()
        payment_result_data3 = PaymentResult.objects.select_related('payment_plan').filter(payment_plan__payment_unit_id=3).select_related('payment_plan__payment_unit').all()
        payment_result_data4 = PaymentResult.objects.select_related('payment_plan').filter(payment_plan__payment_unit_id=4).select_related('payment_plan__payment_unit').all()
        payment_result_data5 = PaymentResult.objects.select_related('payment_plan').filter(payment_plan__payment_unit_id=5).select_related('payment_plan__payment_unit').all()

        #print(vars(payment_result_data1))
        #TODO unit_idを固定値ではなくroopで回す
        #######################################################################################################################
        #どっちが早いか、あとで検証
        #payment_result_data = PaymentResult.objects.select_related('payment_plan').all()
        #payment_result_data1 = payment_result_data.filter(payment_plan__payment_unit_id=1)
        #payment_result_data2 = payment_result_data.filter(payment_plan__payment_unit_id=2)
        #payment_result_data3 = payment_result_data.filter(payment_plan__payment_unit_id=3)
        #payment_result_data4 = payment_result_data.filter(payment_plan__payment_unit_id=4)
        #payment_result_data5 = payment_result_data.filter(payment_plan__payment_unit_id=5)

        #payment_result_data1 = PaymentResult.objects.select_related('payment_plan').filter(payment_plan__payment_unit_id=1)
        #payment_result_data2 = PaymentResult.objects.select_related('payment_plan').filter(payment_plan__payment_unit_id=2)
        #payment_result_data3 = PaymentResult.objects.select_related('payment_plan').filter(payment_plan__payment_unit_id=3)
        #payment_result_data4 = PaymentResult.objects.select_related('payment_plan').filter(payment_plan__payment_unit_id=4)
        #payment_result_data5 = PaymentResult.objects.select_related('payment_plan').filter(payment_plan__payment_unit_id=5)

        #######################################################################################################################

        context = {
            'payment_unit_data1': payment_result_data1,
            'payment_unit_data2': payment_result_data2,
            'payment_unit_data3': payment_result_data3,
            'payment_unit_data4': payment_result_data4,
            'payment_unit_data5': payment_result_data5,
            'payment_unit_count1': len(payment_result_data1),
            'payment_unit_count2': len(payment_result_data2),
            'payment_unit_count3': len(payment_result_data3),
            'payment_unit_count4': len(payment_result_data4),
            'payment_unit_count5': len(payment_result_data5),
            #'unit_data':payment_unit,
            #'planForm': PaymentPlanForm(),
            'resultForm': PaymentResultForm(),
        }

        return render(request, 'budget/index.html', context)

    def post(self, request, *args, **kwargs):
        """POST リクエスト用のメソッド"""
        print(request.POST)
        print(request.POST['memo'])
        #TODO payment_plan_id,amount_plus_flg,family_id,member_id,rank,payment_date
        insert = {
            'payment_plan_id': 1,
            'amount_plus_flg': 1,
            'amount': request.POST['amount'],
            'memo': request.POST['memo'],
            'family_id': 1,
            'member_id': 1,
            'rank': 1,
            'payment_date': request.POST['payment_date'],
        }
        PaymentResult.objects.create(**insert)

        #表示用
        payment_result_data1 = PaymentResult.objects.select_related('payment_plan').filter(payment_plan__payment_unit_id=1).select_related('payment_plan__payment_unit').all()
        payment_result_data2 = PaymentResult.objects.select_related('payment_plan').filter(payment_plan__payment_unit_id=2).select_related('payment_plan__payment_unit').all()
        payment_result_data3 = PaymentResult.objects.select_related('payment_plan').filter(payment_plan__payment_unit_id=3).select_related('payment_plan__payment_unit').all()
        payment_result_data4 = PaymentResult.objects.select_related('payment_plan').filter(payment_plan__payment_unit_id=4).select_related('payment_plan__payment_unit').all()
        payment_result_data5 = PaymentResult.objects.select_related('payment_plan').filter(payment_plan__payment_unit_id=5).select_related('payment_plan__payment_unit').all()

        context = {
            'payment_unit_data1': payment_result_data1,
            'payment_unit_data2': payment_result_data2,
            'payment_unit_data3': payment_result_data3,
            'payment_unit_data4': payment_result_data4,
            'payment_unit_data5': payment_result_data5,
            'payment_unit_count1': len(payment_result_data1),
            'payment_unit_count2': len(payment_result_data2),
            'payment_unit_count3': len(payment_result_data3),
            'payment_unit_count4': len(payment_result_data4),
            'payment_unit_count5': len(payment_result_data5),
            'resultForm': PaymentResultForm(),
        }

        return render(request, 'budget/index.html', context)


index = IndexView.as_view()