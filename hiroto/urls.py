from django.urls import path
from . import views

app_name = 'hiroto'

urlpatterns = [
    #topPage
    path('', views.index, name='index'),
    path('budget', views.index, name='index'),
]
