from django.views.generic import TemplateView
from django.views import View
from .mixin import *
from django.shortcuts import render

#class IndexView(LoginRequiredMixin,TemplateView):
#class IndexView(TemplateView):
#    print(vars(request.session))
#    print("aaaaaaaaaaaaaaaaaaa")
#    template_name = 'hiroto/index.html'
#
#index = IndexView.as_view()

class IndexView(View):
    def get(self,request,*args,**kwargs):
        """GET リクエスト用のメソッド"""
        print("session_get2")
        print(vars(request.session))
        return render(request,'hiroto/index.html')

    def post(self,request,*args,**kwargs):
        """POST リクエスト用のメソッド"""
        print("session_post2")
        print(vars(request.session))
        return render(request,'hiroto/index.html')

index = IndexView.as_view()