from django.contrib import admin
from api.models import Item

# Register your models here.
class ItemAdmin(admin.ModelAdmin):

    # list_display = ['title', 'price', 'like_count', 'full_title','is_active','owner', 'owner_email']
    # search_fields = ['title']
    pass

admin.site.register(Item, ItemAdmin)

