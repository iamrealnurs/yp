from django.views.generic import TemplateView
from django.shortcuts import render

class IndexView(TemplateView):
    template_name = 'main/index.html'
    extra_context = {'greetings' : "Hello New World!!!"}

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['greetings'] = "Hello New World!!!"
    #     return context
