from django.contrib import admin
from api.models import Item, Profile, AssetBundle, Asset, Comment, Like

# Register your models here.
class ItemAdmin(admin.ModelAdmin):

    # list_display = ['title', 'price', 'like_count', 'full_title','is_active','owner', 'owner_email']
    # search_fields = ['title']
    list_display = ['owner', 'title', 'asset_bundle', 'created', 'is_active']
    search_fields = ['title']

admin.site.register(Item, ItemAdmin)

class ProfileAdmin(admin.ModelAdmin):

    list_display = ['user']

admin.site.register(Profile, ProfileAdmin)

class AssetBundleAdmin(admin.ModelAdmin):

    list_display = ['salt', 'kind']

admin.site.register(AssetBundle, AssetBundleAdmin)

class AssetAdmin(admin.ModelAdmin):

    def preview(self, obj):
        return '<img src="{}" width="100">'.format(obj.full_url)

    preview.allow_tags = True

    list_display = ['preview', 'kind', 'extension', 'full_url',]

admin.site.register(Asset, AssetAdmin)

class CommentAdmin(admin.ModelAdmin):

    pass

admin.site.register(Comment, CommentAdmin)

class LikeAdmin(admin.ModelAdmin):

    pass

admin.site.register(Like, LikeAdmin)

