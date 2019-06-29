from django.conf.urls import url,include
from . import views

app_name = 'budget'

urlpatterns = [
    url(r'^average_ajax/', views.for_ajax),
    url('', views.index, name='index'),
]