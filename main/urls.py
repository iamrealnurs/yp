from django.urls import path, include
from .views import IndexView, AdsListView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('ads/', AdsListView.as_view(), name='ads-list'),
]
