from django.contrib import admin
from .models import Advertisment



class AdvertisementAdmin(admin.ModelAdmin):
    list_display =['id','title','description','price','auction','created_date']
    list_filter = ['price','auction','create_at']
    actions = ['make_auction_as_true','make_auction_as_false']
    fieldsets = (
        ('Общие',{
            'fields':('title','description')
        }),
        ('Финанасы',{
            'fields':('price','auction'),
            'classes':['collapse']
        })
    )


    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self,request,queryset):
        queryset.update(auction=True)

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)


admin.site.register(Advertisment,AdvertisementAdmin)