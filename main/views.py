from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from .models import Seller, Category, Tag, Ad
from .forms import UpdateUserForm, UpdateSellerForm, CreateAdForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
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


class SellerUpdateView(LoginRequiredMixin, UpdateView):
    model = Seller
    form_class = UpdateSellerForm
    template_name = "main/seller/update.html"

    def get_login_url(self):
        return '/'

    def get_redirect_field_name(self):
        return ''

    def get_object(self, *args, **kwargs):
        if not self.request.user:
            return redirect('index')
        else:
            current_user = self.request.user
            seller = get_object_or_404(Seller, user=current_user)
            if not seller:
                return redirect('index')

        return seller

    def get_success_url(self, *args, **kwargs):
        return reverse("seller-update")


class AdsUpdateView(UpdateView):
    model = Ad
    form_class = CreateAdForm
    template_name = 'main/ads/update.html'
