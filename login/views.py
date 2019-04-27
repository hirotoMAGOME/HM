from django.shortcuts import render, redirect

from django.views import View
from login.models import Member

from login.forms import LoginForm

from django.views.generic import RedirectView
from django.http import HttpResponseRedirect

# Create your views here.


class LoginView(View):

    def get(self, request, *args, **kwargs):
        """GET リクエスト用のメソッド"""
        context = {
            'form': LoginForm(),
        }
        return render(request, 'login/login.html', context)

    def post(self, request, *args, **kwargs):
        """POST リクエスト用のメソッド"""
        form = LoginForm(request.POST)

        if not form.is_valid():
            print("バリデーションエラー")
            return render(request, 'login/login.html', {'form': form})

        try:
            member_data = Member.objects.get(
                login_id=request.POST["login_id"], password=request.POST["password"], family_id=request.POST['family']
            )

            #login成功したdirへ遷移
            #return HttpResponseRedirect("/" + member_data.first_name_en + "/")

            #一旦、budgetで開発
            return HttpResponseRedirect("/budget/")
        except:
            print("login failure")
            return HttpResponseRedirect("/")


login = LoginView.as_view()


class RedirectLoginView(RedirectView):
    url = '/login/'


index = RedirectLoginView.as_view()
