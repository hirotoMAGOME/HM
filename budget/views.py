from django.shortcuts import render, redirect
from django.views import View

from budget.forms import PaymentPlanForm, PaymentResultForm
from budget.models import PaymentPlan, PaymentResult, PaymentUnit, PaymentCategory, WalletType, Wallet

from datetime import datetime

class IndexView(View):
    def get(self, request, *args, **kwargs):
        """GET リクエスト用のメソッド"""

        #TODO ORMを使う
        #TODO 必要な項目だけをSELECT
        payment_result_data1 = get_front_info(1)
        payment_result_data2 = get_front_info(2)
        payment_result_data3 = get_front_info(3)
        payment_result_data4 = get_front_info(4)
        payment_result_data5 = get_front_info(5)

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
            'planForm': PaymentPlanForm(),
            'resultForm': PaymentResultForm(),
        }

        return render(request, 'budget/index.html', context)

    def post(self, request, *args, **kwargs):
        """POST リクエスト用のメソッド"""
        if 'result_button' in request.POST:
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

        elif 'plan_button' in request.POST:
            #TODO memo項目追加
            update = {
                'amount': request.POST['planform_amount'],
                'family_id': 1,
                'member_id': 1,
                'name': request.POST['planform_name'],
                'payment_limit': request.POST['planform_payment_limit'],
                'payment_unit_id': request.POST['planform_payment_unit_id'],
                'amount_plus_flg': request.POST['planform_amount_plus_flg'],
                'update_date': datetime.now(),
            }
            PaymentPlan.objects.filter(id=request.POST['planform_id']).update(**update)




        #TODO ORMを使う
        #TODO 必要な項目だけをSELECT
        payment_result_data1 = get_front_info(1)
        payment_result_data2 = get_front_info(2)
        payment_result_data3 = get_front_info(3)
        payment_result_data4 = get_front_info(4)
        payment_result_data5 = get_front_info(5)

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
            'planForm': PaymentPlanForm(),
            'resultForm': PaymentResultForm(),
        }

        return render(request, 'budget/index.html', context)

index = IndexView.as_view()


def get_front_info(unit_id):
    from django.db import connection

    #取得項目の順番を変えると、フロントがずれる。
    #TODO 辞書型で取得する。テンプレートのソースがわかりづらい。
    cursor = connection.cursor()
    cursor.execute(
        "SELECT "
        "plan.id,plan.name,plan.payment_limit,plan.amount_plus_flg,plan.amount,result.id,result.payment_date,result.memo,result.amount_plus_flg,result.amount,unit.name_en "
        "FROM payment_plan AS plan "
        "LEFT JOIN payment_unit as unit ON plan.payment_unit_id = unit.id "
        "LEFT JOIN payment_result as result ON plan.id = result.payment_plan_id "
        "WHERE payment_unit_id = %s",
        {unit_id}
    )
    data = cursor.fetchall()

    return data