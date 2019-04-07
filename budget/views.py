from django.shortcuts import render,redirect

from django.views import View
from login.models import Member

from login.forms import LoginForm

from django.views.generic import RedirectView
from django.http import HttpResponseRedirect

# Create your views here.

class LoginView(View):
    def get(self,request,*args,**kwargs):
        """GET リクエスト用のメソッド"""
        context = {
            'form':LoginForm(),
        }
        return render(request,'login/login.html',context)
        print("session_get")
        print(vars(request.session))

    def post(self,request,*args,**kwargs):
        """POST リクエスト用のメソッド"""


login = LoginView.as_view()

class RedirectLoginView(RedirectView):
    url = '/login/'
index = RedirectLoginView.as_view()
