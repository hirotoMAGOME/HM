from django.contrib.auth import login as auth_login
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import View
from login.models import Member

from login.forms import LoginForm

from django.views.generic import RedirectView

# Create your views here.

class LoginView(View):
    def get(self,request,*args,**kwargs):
        """GET リクエスト用のメソッド"""
        context = {
            'form':LoginForm(),
        }
        return render(request,'login/login.html',context)

    def post(self,request,*args,**kwargs):
        """POST リクエスト用のメソッド"""
        form = LoginForm(request.POST)

        if not form.is_valid():
            print("バリデーションエラー")
            return render(request,'login/login.html',{'form':form})
        #user = form.get_user()

        success_count = Member.objects.filter(login_id = request.POST["login_id"],password = request.POST["password"]).count()#0件時のエラー処理
        if success_count==1:
            print("login success")
            #return render(reverse("login:hiroto"))
            return render(request, 'hiroto/index.html')
        else:
            print("login faild")

        #auth_login(request,user)

        return render(request,'login/login.html')

login = LoginView.as_view()

class RedirectLoginView(RedirectView):
    url = '/login/'

index = RedirectLoginView.as_view()
