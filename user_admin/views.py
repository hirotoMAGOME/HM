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

def for_ajax_config1(request):
    import json
    from django.http import HttpResponse,Http404
    print("config1")
    print(request.POST)
    if request.method == 'POST':
        print("config_ajax")
        response = json.dumps({'aaaaaaa': 'bbbbbb',})
        return HttpResponse(response)
    else:
        print("config_ajax_bbb")
        raise Http404