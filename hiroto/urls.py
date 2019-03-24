from django.urls import path
from . import views

app_name = 'hiroto'

urlpatterns = [
    #topPage
    path('', views.index, name='index'),
    path('aa', views.index, name='index'),
]
