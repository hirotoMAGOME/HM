from django.shortcuts import render, redirect
from django.views import View

from budget.forms import PaymentPlanRegistForm, PaymentPlanUpdateForm, PaymentResultRegistForm, PaymentResultUpdateForm, DisplayForm, SettlementForm, WalletUpdateForm
from budget.models import PaymentPlan, PaymentResult, Wallet, WalletHistory, DoublePost, Settlement

from django.db import connection
from datetime import datetime, timedelta
import calendar

class IndexView(View):
    def get(self, request, *args, **kwargs):
        """GET リクエスト用のメソッド"""
        """TODO 対象月プルダウンでの絞り込み"""
        print("get")
        if 'month_select_box' in request.GET:
            disp_month = request.GET['month_select_box']
        else:
            disp_month = datetime.today().month

        """出力情報の取得"""
        context = get_disp_data(disp_month)

        return render(request, 'budget/index.html', context)

    def post(self, request, *args, **kwargs):
        """POST リクエスト用のメソッド"""

        #TODO 2重POSTの防止　同じPOSTがきた場合は、処理しない。
        # 古いデータの削除(1日以上古いデータを削除)
        delete_limit = datetime.now() - timedelta(days=1)
        dp_del = DoublePost.objects.filter(create_date__lte=delete_limit)
        dp_del.delete()

        #2重とみなす時間(s)
        double_post_error_period = 1200
        double_min_time = datetime.now() - timedelta(seconds=double_post_error_period)
        double_max_time = datetime.now() + timedelta(seconds=double_post_error_period)

        #2重チェック用のPOSTデータ
        check_csrf = request.POST['csrfmiddlewaretoken']
        check_post_text = ''
        for post_key in request.POST:
            check_post_text = check_post_text + request.POST[post_key]

        dp = DoublePost.objects.filter(
            create_date__gte=double_min_time,
            create_date__lte=double_max_time,
            csrf=check_csrf,
            post_text=check_post_text,
        )
        if len(dp) > 0:
            print("2重POSTあり")
            return render(request, 'budget/index.html', context)

        print("post")
        if 'result_regist_button' in request.POST:
            print('result_regist_button')

            #TODO family_id,member_id,rank
            insert = {
                'payment_plan_id': request.POST['PRRF_selected_plan_id'],
                'amount_plus_flg': request.POST['PRRF_amount_plus_flg'],
                'amount': request.POST['PRRF_amount'],
                'memo': request.POST['PRRF_memo'],
                'family_id': 1,
                'member_id': 1,
                'rank': 1,
                'payment_date': request.POST['PRRF_payment_date'],
            }
            PaymentResult.objects.create(**insert)

            # Wallet
            diff_amount = request.POST['PRRF_amount'] if(request.POST['PRRF_amount_plus_flg'] == '1') else int(request.POST['PRRF_amount']) * (-1)
            update_wallet(request.POST['PRRF_wallet'], diff_amount, 2)

            #2重チェック用
            insert = {
                'csrf': request.POST['csrfmiddlewaretoken'],
                'post_text': check_post_text,
                'create_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            DoublePost.objects.create(**insert)

        elif 'result_update_button' in request.POST:
            print('result_update_button')

            # TODO family_id,member_id,rank
            update = {
                'amount_plus_flg': request.POST['PRUF_amount_plus_flg'],
                'amount': request.POST['PRUF_amount'],
                'memo': request.POST['PRUF_memo'],
                'family_id': 1,
                'member_id': 1,
                'rank': 1,
                'payment_date': request.POST['PRUF_payment_date'],
            }
            PaymentResult.objects.filter(id=request.POST['PRUF_selected_result_id']).update(**update)
            print('実績を更新しました。result_id = ' + request.POST['PRUF_selected_result_id'])

        elif 'plan_regist_button' in request.POST:
            print('plan_regist_button')
            #TODO memo項目追加
            update = {
                'amount': request.POST['PPRF_planform_amount'],
                'family_id': 1,
                'member_id': 1,
                'name': request.POST['PPRF_planform_name'],
                'payment_limit': request.POST['PPRF_planform_payment_limit'],
                'payment_unit_id': request.POST['PPRF_planform_payment_unit_id'],
                'amount_plus_flg': request.POST['PPRF_planform_amount_plus_flg'],
                'update_date': datetime.now(),
            }
            PaymentPlan.objects.filter(id=request.POST['PPRF_planform_id']).update(**update)

        elif 'plan_update_button' in request.POST:
            print('plan_update_button')
            #TODO memo項目追加
            update = {
                'amount': request.POST['PPUF_planform_amount'],
                'family_id': 1,
                'member_id': 1,
                'name': request.POST['PPUF_planform_name'],
                'payment_limit': request.POST['PPUF_planform_payment_limit'],
                'payment_unit_id': request.POST['PPUF_planform_payment_unit_id'],
                'amount_plus_flg': request.POST['PPUF_planform_amount_plus_flg'],
                'update_date': datetime.now(),
            }
            PaymentPlan.objects.filter(id=request.POST['PPUF_planform_id']).update(**update)
            print('予算を更新しました。result_id = ' + request.POST['PPUF_planform_id'])

        elif 'wallet_button' in request.POST:
            print('wallet_button')
            print(request.POST)
            #入力された残高を更新する

            update_wallet_id = request.POST['asset_id']
            update_wallet_balance = request.POST['balance']

            # idと金額でWalletの更新とWalletHistoryの作成
            update_wallet(update_wallet_id, update_wallet_balance, 1)

        elif 'settlement_button' in request.POST:
            print('settlement_button')
            update_settlement(request.POST['settlement_month'], request.POST['settlement_date'])


        """TODO 対象月プルダウンでの絞り込み"""
        if 'month_select_box' in request.GET:
            disp_month = request.GET['month_select_box']
        else:
            disp_month = datetime.today().month

        """表示内容の
        
        取得"""
        context = get_disp_data(disp_month)


        return render(request, 'budget/index.html', context)

index = IndexView.as_view()


def get_front_info(unit_id, month):

    #取得項目の順番を変えると、フロントがずれる。
    #TODO 辞書型で取得する。テンプレートのソースがわかりづらい。
    cursor = connection.cursor()
    cursor.execute(
        "SELECT "
        "plan2.id as id,plan2.name as name,plan2.payment_limit as payment_limit,plan2.amount_plus_flg as anount_plus_flg,plan2.amount as amount,result2.id as result_id,result2.payment_date as payment_date,result2.memo as memo,result2.amount_plus_flg as result_amount_plus_flg,result2.amount as result_amount,unit.name_en as name_en,1 as sample_flg "
        "FROM payment_plan AS plan2 "
        "LEFT JOIN payment_unit as unit ON plan2.payment_unit_id = unit.id "
        "LEFT JOIN payment_result_sample as result2 ON plan2.id = result2.payment_plan_id "
        "WHERE payment_unit_id = %s "
        "AND result2.id IS NOT NULL "
        "UNION ALL "
        "SELECT "
        "plan.id as id,plan.name as name,plan.payment_limit as payment_limit,plan.amount_plus_flg as anount_plus_flg,plan.amount as amount,result.id as result_id,result.payment_date as payment_date,result.memo as memo,result.amount_plus_flg as result_amount_plus_flg,result.amount as result_amount,unit.name_en as name_en,0 as sample_flg "
        "FROM payment_plan AS plan "
        "LEFT JOIN payment_unit as unit ON plan.payment_unit_id = unit.id "
        "LEFT JOIN payment_result as result ON plan.id = result.payment_plan_id "
        "WHERE payment_unit_id = %s "
        "AND result.id IS NOT NULL "
        "ORDER BY id ASC,sample_flg DESC"
        , (unit_id, unit_id,)
    )
    data = cursor.fetchall()

    return data


def for_ajax_average(request):
    import json
    from django.http import HttpResponse,Http404

    if request.method == 'POST' and 'average_plan_id' in request.POST:
        plan_id = request.POST['average_plan_id']

        #plan_idに紐付く実績収支の平均を出す
        cursor = connection.cursor()
        cursor.execute(
            "SELECT "
            "ROUND(AVG(amount),0) as average "
            "FROM payment_result "
            "WHERE payment_plan_id = %s "
            , (plan_id,)
        )
        data = cursor.fetchall()

        #出力結果から平均金額を取得
        average_price = int(data[0][0])

        #レスポンスを返す
        response = json.dumps({'average_price': average_price,})
        return HttpResponse(response)
    else:
        raise Http404


def get_disp_data(disp_month):
    #各予算単位ごとにデータの取得
    payment_result_data1 = get_front_info(1, disp_month)
    payment_result_data2 = get_front_info(2, disp_month)
    payment_result_data3 = get_front_info(3, disp_month)
    payment_result_data4 = get_front_info(4, disp_month)
    payment_result_data5 = get_front_info(5, disp_month)

    #合計金額を計算
    total_plan = 0
    total_result = 0
    for data in payment_result_data1:
        if data[11] == 0:
            total_result = total_result - data[9] + (data[9] * data[8] * 2)
        elif data[11] == 1:
            total_plan = total_plan - data[4] + (data[4] * data[3] * 2)
    for data in payment_result_data2:
        if data[11] == 0:
            total_result = total_result - data[9] + (data[9] * data[8] * 2)
        elif data[11] == 1:
            total_plan = total_plan - data[4] + (data[4] * data[3] * 2)
    for data in payment_result_data3:
        if data[11] == 0:
            total_result = total_result - data[9] + (data[9] * data[8] * 2)
        elif data[11] == 1:
            total_plan = total_plan - data[4] + (data[4] * data[3] * 2)
    for data in payment_result_data4:
        if data[11] == 0:
            total_result = total_result - data[9] + (data[9] * data[8] * 2)
        elif data[11] == 1:
            total_plan = total_plan - data[4] + (data[4] * data[3] * 2)
    for data in payment_result_data5:
        if data[11] == 0:
            total_result = total_result - data[9] + (data[9] * data[8] * 2)
        elif data[11] == 1:
            total_plan = total_plan - data[4] + (data[4] * data[3] * 2)

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
        'total_result': total_result,
        'total_plan': total_plan,
        'planRegistForm': PaymentPlanRegistForm(),
        'planUpdateForm': PaymentPlanUpdateForm(),
        'resultRegistForm': PaymentResultRegistForm(),
        'resultUpdateForm': PaymentResultUpdateForm(),
        'displayForm': DisplayForm(),
        'disp_month': disp_month,
        'wallet_data': wallet_data,
        'walletUpdateForm': WalletUpdateForm(),
        'settlementForm': SettlementForm(),
    }

    return context


# 財布の金額を更新
# 更新前の金額はWalletHistoryにコピー
# update_wallet_id
# update_balance
# mode 1:balance=update_balanceで更新　2:balance = balance + update_balanceで更新
def update_wallet(update_wallet_id, update_balance, mode):
    wallet = Wallet.objects.filter(id=update_wallet_id).values('id', 'balance', 'family_id', 'member_id', 'create_date')

    # Walletの内容をWalletHistoryでUPDATE
    wh = WalletHistory(
        balance=wallet[0]['balance'],
        family_id=wallet[0]['family_id'],
        member_id=wallet[0]['member_id'],
        create_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        update_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        del_flg=0,
        wallet_id_id=wallet[0]['id'],
    )
    wh.save()

    if mode == 1:
        new_balance = update_balance
    elif mode == 2:
        new_balance = int(wallet[0]['balance']) + int(update_balance)

    # Walletを更新
    Wallet.objects.filter(id=update_wallet_id).update(balance=new_balance,
                                                      update_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def update_settlement(month,date):

    #成形
    settlement_month = month[0:4] + '-' + month[4:6] + '-01 00:00:00'
    settlement_date = date[0:4] + '-' + date[4:6] + '-' + date[6:8] + ' 00:00:00'

    # TODO 重複チェック
    # INSERT 実行
    insert = {
        'settlement_month': settlement_month,
        'settlement_date': settlement_date,
        'family_id': 1,
        'member_id': 1,
        'create_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'update_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    Settlement.objects.create(**insert)

    # UPDATE 内容の設定
    first_date = settlement_month
    _, last = calendar.monthrange(int(month[0:4]), int(month[4:6].replace('0', '')))
    last_date = month[0:4] + '-' + month[4:6] + '-' + str(last) + ' 23:59:59'

    update = {
        'payment_month': first_date,
        'update_date': datetime.now(),
    }

    # UPDATE 実行
    PaymentResult.objects.filter(
        payment_month__isnull=True,
        payment_date__gte=first_date,
        payment_date__lte=last_date,
    ).update(**update)
