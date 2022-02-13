from django.urls import path, include
from .views import IndexView, AdsListView, AdsDetailView, SellerUpdateView, AdsUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('ads/', AdsListView.as_view(), name='ads-list'),
    path('ads/<int:pk>/', AdsDetailView.as_view(), name='ads-detail'),
    path('ads/<int:pk>/edit/', AdsUpdateView.as_view(), name='ads-edit'),
    path('accounts/seller/', SellerUpdateView.as_view(), name='seller-update'),
]
