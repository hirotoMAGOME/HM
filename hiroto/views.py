from django.views.generic import TemplateView
from .mixin import *
from django.shortcuts import render


#class IndexView(LoginRequiredMixin,TemplateView):
class IndexView(TemplateView):
    def get(self,request):
        print(vars(request.session))
    template_name = 'hiroto/index.html'

index = IndexView.as_view()