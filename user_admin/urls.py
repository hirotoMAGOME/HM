from django.conf.urls import url,include
from . import views

app_name = 'user_admin'

urlpatterns = [
    url('', views.index, name='index'),
]