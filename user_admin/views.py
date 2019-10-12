from django.shortcuts import render, redirect
from django.views import View
from django.db import connection
from user_admin.models import UserAdminConfig

class IndexView(View):
    def get(self, request, *args, **kwargs):
        """GET リクエスト用のメソッド"""
        print("get")

        """取得情報の取得"""
        config_data = UserAdminConfig.objects.order_by('rank').values('name', 'memo', 'value', 'rank')
        context={
            'config_data': config_data,
        }
        return render(request, 'user_admin/index.html', context)

    def post(self, request, *args, **kwargs):
        """POST リクエスト用のメソッド"""
        context={
            'aaa': "kkk",
        }
        return render(request, 'budget/index.html', context)


index = IndexView.as_view()

"""
平均金額を返せるかどうか判断する関数

@param request={
        "average_plan_id": (int),
        "csrfmiddlewaretoken": (str),
    }
@return 0 (平均金額表示対象)
        1 (平均金額表示対象外)
"""
def for_ajax_config1(request):
    import json
    from django.http import HttpResponse,Http404

    if request.method == 'POST' and 'average_plan_id' in request.POST:
        plan_id = request.POST['average_plan_id']

        #plan_idに紐付く実績収支の平均を出す
        cursor = connection.cursor()
        cursor.execute(
            "SELECT "
            "value "
            "FROM user_admin_config "
            "WHERE name = concat( "
                "'AVERAGE_PER_'"
                ",UPPER("
                    "(SELECT name_en FROM payment_unit WHERE id = (SELECT payment_unit_id FROM payment_plan WHERE id = %s))"
                ")"
            ")"
            , (plan_id,)
        )
        data = cursor.fetchall()
    else:
        raise Http404


    #出力結果から平均金額を取得できる場合は0を返す
    if len(data) != 0:
        plan_ids = data[0][0].split(',')

        if plan_id in plan_ids:
            # レスポンスを返す
            response = json.dumps({'success_flg': 0, })
            return HttpResponse(response)
        else:
            # レスポンスを返す
            response = json.dumps({'success_flg': 1, })
            return HttpResponse(response)

    else:
        # レスポンスを返す
        response = json.dumps({'success_flg': 1, })
        return HttpResponse(response)


"""
請求月を表示させるかどうかを判断し、必要情報をフロントへ返す関数
TODO 請求月に限らず、金額も全部返せば、フロントのjs不要


@param request={
        "request_plan_id": (int),
        "csrfmiddlewaretoken": (str),
    }
@return charge_month ()
        success_flg ()
        payment_result_id ()
"""
def for_ajax_config2(request):
    import json
    from django.http import HttpResponse,Http404

    if request.method == 'POST' and 'request_result_id' in request.POST:
        result_id = request.POST['request_result_id']


        #TODO result_idが果たして月次処理用の実績なのか。
        plan_id = result_to_plan(result_id)
        checksql = check_user_admin_config(6,plan_id)

        if checksql == 0:

            #plan_idに紐付く実績収支の平均を出す
            cursor = connection.cursor()
            cursor.execute(
                "SELECT "
               "charge_month "
                "FROM payment_result "
                "WHERE id = %s "
                , (result_id,)
            )
            data = cursor.fetchall()

            # 出力結果を返す
            if len(data) != 0:
                # resultにレコードが存在した時
                response = json.dumps(
                    {'charge_month': data[0][0].strftime("%m"), 'success_flg': 0, 'payment_result_id': result_id})
                return HttpResponse(response)


            else:
                # resultにレコードが存在しなかったとき
                response = json.dumps({'success_flg': 1, })
                return HttpResponse(response)

        else:
            print("error")

    else:
        raise Http404





def get_day_average(day_plan_id):
    print("get_day_average")

    return day_plan_id


#check_valueが
#user_admin_config_id(int)
#check_value (text)
def check_user_admin_config(user_admin_config_id,check_value):
    #

    # plan_idに紐付く実績収支の平均を出す
    cursor = connection.cursor()
    cursor.execute(
        "SELECT "
        "count(id) "
        "FROM user_admin_config "
        "WHERE id = %s and value LIKE %%s% "
        , (user_admin_config_id,check_value)
    )
    data = cursor.fetchall()

    print(data[0])
    if data[0] > 0:
        print("aaa")
        return 0
    elif data[0] == 0:
        print("bbb")
        return 1
    else:
        print("ccc")
        return 1


def result_to_plan(result_id):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT "
        "payment_plan_id "
        "FROM payment_result "
        "WHERE id = %s"
        , (result_id)
    )
    data = cursor.fetchall()

    if len(data) != 0:
        return data[0]
