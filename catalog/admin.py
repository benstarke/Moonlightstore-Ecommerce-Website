from django.contrib import admin
from django.contrib.auth.models import User,Group
from .models import *

from django.contrib import admin

from .models import Item, Review


class ReviewInline(admin.TabularInline):
    """Tabular Inline View for Product Reviews"""
    model = Review



class ItemAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}
	list_display = [
		'title',
		'price',
		'discount_price'
	]
	list_filter = ('title', 'category',)
	inlines = [
		ReviewInline,
		]



admin.site.unregister(Group)
admin.site.site_header=('MoonLightStore Enterprise')
admin.site.register(Item,ItemAdmin)
#admin.site.register(delivery_order)
admin.site.register(Order)
admin.site.register(delivery)
admin.site.register(contact)
admin.site.register(OrderItem)
admin.site.register(slider)
admin.site.register(about)
admin.site.register(about1)
admin.site.register(addition_info)


