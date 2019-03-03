from django.urls import path
from hiro.migrations import views

urlpatterns = [
#topPage
    path('', views.index, name='index'),
]
