from django.shortcuts import render, redirect
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        """GET リクエスト用のメソッド"""
        print("get")
        context={
            'aaa': "kkk",
        }
        return render(request, 'user_admin/index.html', context)

    def post(self, request, *args, **kwargs):
        """POST リクエスト用のメソッド"""
        context={
            'aaa': "kkk",
        }
        return render(request, 'budget/index.html', context)


index = IndexView.as_view()


