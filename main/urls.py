from django.urls import path, include
from .views import IndexView, AdsListView, AdsDetailView, SellerUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('ads/', AdsListView.as_view(), name='ads-list'),
    path('ads/<int:pk>/', AdsDetailView.as_view(), name='ads-detail'),
    path('accounts/seller/', SellerUpdateView.as_view(), name='seller-update'),
]
