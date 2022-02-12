from django.views.generic import TemplateView, ListView, DetailView
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
    template_name = 'main/ads/list.html'
    paginate_by = 5

    def get_queryset(self):
        print('-------------------')
        print(self.request.GET)
        tag = self.request.GET.get('tag', '')
        if tag:
            query_tag = Tag.objects.get(name=tag)
            queryset = Ad.objects.filter(tags__in=[query_tag])
        else:
            queryset = Ad.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(AdsListView, self).get_context_data(**kwargs)
        tag = self.request.GET.get('tag', '')
        if tag:
            query_tag = Tag.objects.get(name=tag)
            context['query_tag'] = query_tag
        context['all_tags_list'] = list(Tag.objects.all())
        return context


    

class AdsDetailView(DetailView):
    model = Ad
    template_name = 'main/ads/detail.html'

