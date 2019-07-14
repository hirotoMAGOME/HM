from django.conf.urls import url,include
from . import views

app_name = 'user_admin'

urlpatterns = [
    url(r'^config1/', views.for_ajax_config1),
    url('', views.index, name='index'),
]