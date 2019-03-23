from django.conf.urls import url
#from django.contrib.auth.views import login,logout
from . import views

app_name = 'login'
urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url('', views.login, name='login'),
#    url(r'^logout/$', logout, name='logout')
]