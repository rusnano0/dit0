from django.contrib import admin
from api.models import Item

# Register your models here.
class ItemAdmin(admin.ModelAdmin):

    list_display = ['title', 'price', 'like_count', 'full_title','is_active','owner']
    search_fields = ['title']

admin.site.register(Item, ItemAdmin)

