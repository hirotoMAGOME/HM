from django.conf.urls import url,include
from . import views

app_name = 'login'

urlpatterns = [
    url('login/', views.login, name='login'),
    #login/へリダイレクトする
    url('', views.index, name='index'),
]