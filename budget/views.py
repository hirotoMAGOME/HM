from django.shortcuts import render, redirect
from django.views import View

from budget.forms import PaymentPlanForm, PaymentResultForm, DisplayForm
from budget.models import PaymentPlan, PaymentResult, Wallet, WalletHistory

from datetime import datetime
from django.db import connection

class IndexView(View):
    def get(self, request, *args, **kwargs):
        """GET リクエスト用のメソッド"""
        """TODO 対象月プルダウンでの絞り込み"""
        print("get")
        if 'month_select_box' in request.GET:
            disp_month = request.GET['month_select_box']
        else:
            disp_month = datetime.today().month

        context = get_disp_data(disp_month)

        return render(request, 'budget/index.html', context)

    def post(self, request, *args, **kwargs):
        """POST リクエスト用のメソッド"""
        """TODO 対象月プルダウンでの絞り込み"""
        if 'month_select_box' in request.GET:
            disp_month = request.GET['month_select_box']
        else:
            disp_month = datetime.today().month

        context = get_disp_data(disp_month)

        print("post")
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

        elif 'wallet_button' in request.POST:
            #入力された残高を更新する
            for post_key in request.POST:
                if post_key[0:15] == 'balance_update_' and len(request.POST[post_key]) != 0:
                    update_wallet_id = post_key.replace('balance_update_', '')
                    wallet = Wallet.objects.filter(id=update_wallet_id).values('id', 'balance', 'family_id', 'member_id', 'create_date')

                    #Walletの内容をWalletHistoryでUPDATE
                    wh = WalletHistory(
                        balance=wallet[0]['balance'],
                        family_id=wallet[0]['family_id'],
                        member_id=wallet[0]['member_id'],
                        create_date=wallet[0]['create_date'],
                        update_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        del_flg=0,
                        wallet_id_id=wallet[0]['id'],
                    )
                    wh.save()

                    #Walletを更新
                    Wallet.objects.filter(id=update_wallet_id).update(balance=request.POST[post_key], update_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        return render(request, 'budget/index.html', context)

index = IndexView.as_view()


def get_front_info(unit_id, month):

    #取得項目の順番を変えると、フロントがずれる。
    #TODO 辞書型で取得する。テンプレートのソースがわかりづらい。
    cursor = connection.cursor()
    cursor.execute(
        "SELECT "
        "plan.id,plan.name,plan.payment_limit,plan.amount_plus_flg,plan.amount,result.id,result.payment_date,result.memo,result.amount_plus_flg,result.amount,unit.name_en "
        "FROM payment_plan AS plan "
        "LEFT JOIN payment_unit as unit ON plan.payment_unit_id = unit.id "
        "LEFT JOIN payment_result as result ON plan.id = result.payment_plan_id "
        "WHERE payment_unit_id = %s "
        "AND MONTH(payment_date) = %s",
        (unit_id, month, )
    )
    data = cursor.fetchall()

    return data


def get_disp_data(disp_month):
    #各予算単位ごとにデータの取得
    payment_result_data1 = get_front_info(1, disp_month)
    payment_result_data2 = get_front_info(2, disp_month)
    payment_result_data3 = get_front_info(3, disp_month)
    payment_result_data4 = get_front_info(4, disp_month)
    payment_result_data5 = get_front_info(5, disp_month)

    #各資産ごとの残高を取得
    wallet_data = Wallet.objects.all()

    #取得したデータを配列にセット
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
        'displayForm': DisplayForm(),
        'disp_month': disp_month,
        'wallet_data': wallet_data,
    }

    return context
