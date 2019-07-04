from django.conf.urls import url,include
from . import views

app_name = 'budget'

urlpatterns = [
    url(r'^average_ajax/', views.for_ajax_average),
    url('', views.index, name='index'),
]