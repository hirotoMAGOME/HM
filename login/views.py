from django.shortcuts import render

from django.views import View

from django.views.generic import TemplateView
# Create your views here.

class LoginView(View):
    #template_name = 'login/login.html'
#login = LoginView.as_view()

    def get(self,request,*args,**kwargs):
            context = {
                'message':"Hello World!",
            }
            return render(request,'login/login.html',context)
login = LoginView.as_view()