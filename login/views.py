from django.shortcuts import render,redirect

from django.views import View
from login.models import Member

from login.forms import LoginForm

from django.views.generic import RedirectView
from django.http import HttpResponseRedirect

from datetime import datetime

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
        form = LoginForm(request.POST)

        if not form.is_valid():
            print("バリデーションエラー")
            return render(request,'login/login.html',{'form':form})

        try:
            member_data = Member.objects.get(login_id = request.POST["login_id"],password = request.POST["password"])
            print("login success")
            request.session['login_id'] = request.POST['login_id']
            #request.session['time'] = datetime.now
            #request.session.save()
            print("session_post")
            print(vars(request.session))
            return HttpResponseRedirect(member_data.first_name_en + "/")
        except:
            print("login failure")
            return HttpResponseRedirect("/")

login = LoginView.as_view()

class RedirectLoginView(RedirectView):
    url = '/login/'
index = RedirectLoginView.as_view()
