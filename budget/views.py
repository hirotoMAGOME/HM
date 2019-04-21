from django.shortcuts import render,redirect

from django.views import View


# Create your views here.

class IndexView(View):
    def get(self,request,*args,**kwargs):
        """GET リクエスト用のメソッド"""
#        context = {
#            'form':LoginForm(),
#        }
        return render(request,'budget/index.html',)

    def post(self,request,*args,**kwargs):
        """POST リクエスト用のメソッド"""


index = IndexView.as_view()