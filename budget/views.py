from django.shortcuts import render, redirect
from django.views import View

from budget.forms import PaymentResultForm

from budget.models import PaymentPlan, PaymentResult, PaymentUnit, PaymentCategory, WalletType, Wallet

from django.db import connection

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

        #cursor1 = connection.cursor()
        #cursor1.execute("SELECT * FROM payment_plan  AS plan LEFT JOIN payment_unit as unit ON plan.payment_unit_id = unit.id LEFT JOIN payment_result as result ON plan.id = result.payment_plan_id WHERE payment_unit_id = 1")
        #payment_result_data1 = cursor1.fetchall()
        #cursor2 = connection.cursor()
        #cursor2.execute("SELECT * FROM payment_plan  AS plan LEFT JOIN payment_unit as unit ON plan.payment_unit_id = unit.id LEFT JOIN payment_result as result ON plan.id = result.payment_plan_id WHERE payment_unit_id = 2")
        #payment_result_data2 = cursor2.fetchall()
        #cursor3 = connection.cursor()
        #cursor3.execute("SELECT * FROM payment_plan  AS plan LEFT JOIN payment_unit as unit ON plan.payment_unit_id = unit.id LEFT JOIN payment_result as result ON plan.id = result.payment_plan_id WHERE payment_unit_id = 3")
        #payment_result_data3 = cursor3.fetchall()
        #cursor4 = connection.cursor()
        #cursor4.execute("SELECT * FROM payment_plan  AS plan LEFT JOIN payment_unit as unit ON plan.payment_unit_id = unit.id LEFT JOIN payment_result as result ON plan.id = result.payment_plan_id WHERE payment_unit_id = 4")
        #payment_result_data4 = cursor4.fetchall()
        #cursor5 = connection.cursor()
        #cursor5.execute("SELECT * FROM payment_plan  AS plan LEFT JOIN payment_unit as unit ON plan.payment_unit_id = unit.id LEFT JOIN payment_result as result ON plan.id = result.payment_plan_id WHERE payment_unit_id = 5")
        #payment_result_data5 = cursor5.fetchall()

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
            'resultForm': PaymentResultForm(),
        }

        return render(request, 'budget/index.html', context)

    def post(self, request, *args, **kwargs):
        """POST リクエスト用のメソッド"""

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
        "plan.name,plan.payment_limit,plan.amount_plus_flg,plan.amount,result.id,result.payment_date,result.memo,result.amount_plus_flg,result.amount,unit.name_en "
        "FROM payment_plan AS plan "
        "LEFT JOIN payment_unit as unit ON plan.payment_unit_id = unit.id "
        "LEFT JOIN payment_result as result ON plan.id = result.payment_plan_id "
        "WHERE payment_unit_id = %s",
        {unit_id}
    )
    data = cursor.fetchall()

    return data