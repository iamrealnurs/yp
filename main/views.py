from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView, UpdateView,  CreateView
from django.views.generic.edit import UpdateView as UpdateViewForSeller
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Seller, Category, Tag, Ad
from .forms import UpdateUserForm, UpdateSellerForm, AdForm, AdPictureInlineFormset
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from pprint import pprint
from constance import config
from django.forms import modelformset_factory


class HeaderView(TemplateView):
    template_name = 'main/includes/header.html'

    def get_context_data(self, **kwargs):
        context = super(HeaderView, self).get_context_data(**kwargs)
        return context


class IndexView(HeaderView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['greetings'] = 'Hello New World!!!'
        context['turn_on_block'] = config.MAINTENANCE_MODE
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


class UpdateAdsView(UpdateView):
    model = Ad
    form_class = AdForm
    template_name = 'main/ads/edit.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateAdsView, self).get_context_data(**kwargs)
        context['ads_picture_formset'] = AdPictureInlineFormset()
        context['title'] = 'Update AD'
        return context

    def post(self, request, *args, **kwargs):
        ads_picture_formset = AdPictureInlineFormset(self.request.POST, self.request.FILES, instance=self.get_object())
        if ads_picture_formset.is_valid():
            ads_picture_formset.save()
            return HttpResponseRedirect(self.get_success_url())
        return super().post(request, *args, **kwargs)


class CreateAdsView(CreateView):
    form_class = AdForm
    template_name = 'main/ads/edit.html'

    def get_context_data(self, **kwargs):
        context = super(CreateAdsView, self).get_context_data(**kwargs)
        context['ads_picture_formset'] = AdPictureInlineFormset()
        context['title'] = 'Create AD'
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        # form_class = self.form_class
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()
            ads_picture_formset = AdPictureInlineFormset(self.request.POST, self.request.FILES, instance=self.object)
            if ads_picture_formset.is_valid():
                ads_picture_formset.save()
                return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)


class SellerUpdateView(LoginRequiredMixin, UpdateViewForSeller):
    model = Seller
    form_class = UpdateSellerForm
    form_user = UpdateUserForm
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

    def get_context_data(self, **kwargs):
        context = super(SellerUpdateView, self).get_context_data(**kwargs)
        context['form_user'] = self.form_user(self.request.POST, instance=self.object.user)
        return context

    def form_valid(self, form):
        form_user = self.form_user(self.request.POST, instance=self.object.user)
        if form.is_valid() and form_user.is_valid():
            form_user.save()
        else:
            return reverse("seller-update")

        return super().form_valid(form)
