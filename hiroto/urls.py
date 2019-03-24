from django.urls import path
from . import views

app_name = 'hiroto'

urlpatterns = [
    #topPage
    path('hiroto', views.index, name='index'),
]
