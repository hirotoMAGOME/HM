from django.views.generic import TemplateView
from django.views import View
from login.models import Member
from django.shortcuts import render

class IndexView(View):
    def get(self,request,*args,**kwargs):
        """ログインチェック"""
        """
        try:
            print(request.session.session_key)
            member_data = Member.objects.get(session_id=request.session.session_key)
            print("login:")
        except:
            print("login miss:")
            return render(request, 'login/login.html')#リダイレクトのさせ方に不備。現状は/hirotoのままでloginのテンプレートが当たる
        """

        """GET リクエスト用のメソッド"""
        #print("session_get2")
        #print(vars(request.session))
        return render(request,'hiroto/index.html')

    def post(self,request,*args,**kwargs):
        """POST リクエスト用のメソッド"""
        #print("session_post2")
        #print(vars(request.session))
        return render(request,'hiroto/index.html')

index = IndexView.as_view()