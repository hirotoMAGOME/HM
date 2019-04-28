from django.conf.urls import url,include
from . import views

app_name = 'budget'

urlpatterns = [
    #url(r'^budget$', views.index, name='index'),
    url('', views.index, name='index'),
]