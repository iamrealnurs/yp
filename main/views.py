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

    # def get_queryset(self):
    #     # tag = self.kwargs.get("category")
    #     if category:
    #         queryset = Product.objects.filter(category__iexact=category)
    #     else:
    #         queryset = Product.objects.all()
    #     return queryset

    def get_queryset(self):
        q = self.request.GET.get('tag', '')
        if q:
            query_tag = Tag.objects.filter(name=q).first()
            queryset = Ad.objects.filter(tags__in=[query_tag])
        else:
            queryset = Ad.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(AdsListView, self).get_context_data(**kwargs)
        context['all_tags_list'] = list(Tag.objects.all())
        return context


    

class AdsDetailView(DetailView):
    model = Ad
    template_name = 'main/ads/detail.html'

