from django.views.generic import TemplateView, ListView
from .models import Seller, Category, Tag, Ad
from django.shortcuts import render
from pprint import pprint
from constance import config


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['greetings'] = 'Hello New World!!!'
        context['turn_on_block'] = config.MAINTENANCE_MODE
        context['username'] = self.request.user.username
        return context


class AdsListView(ListView):
    model = Ad
    queryset = Ad.objects.all()
    template_name = 'main/ads/list.html'
