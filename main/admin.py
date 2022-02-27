from django.contrib import admin
from .models import Seller, Category, Tag, Ad, Picture
import django.apps


class SellerAdmin(admin.ModelAdmin):
    list_display = ('user', 'actual_ads', 'archived_ads',)

    def actual_ads(self, obj):
        return f'{len(obj.num_ads["actual"])}'
    actual_ads.short_description = 'Actual Ads'

    def archived_ads(self, obj):
        return f'{len(obj.num_ads["archived"])}'
    archived_ads.short_description = 'Archived Ads'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'ads_amount',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AdAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'seller', 'created_at', 'updated_at', 'archived')


admin.site.register(Seller, SellerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Ad, AdAdmin)
admin.site.register(Picture)
#
#
# for model in django.apps.apps.get_models():
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass
