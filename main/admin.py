from django.contrib import admin
from .models import Seller, Category, Tag, Ads


class SellerAdmin(admin.ModelAdmin):
    list_display = ('user', 'ads_amount',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'ads_amount',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)


class AdsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category', 'seller', 'created_at', 'updated_at',)


admin.site.register(Seller, SellerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Ads, AdsAdmin)
