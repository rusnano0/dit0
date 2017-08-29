from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    """ This is the user profile model """
    user = models.OneToOneField(User) # 121 - To keep the same pk's of profile and user
    bio = models.TextField(blank=True, null=True)
    website_url = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username

class AssetBundle(models.Model):
    """
    This is the Asset Bundle model

    http://CDN.com/uploads/{ab_kind}/{ab_salt}_{a_kind}.{a_extension}
    """

    KIND_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )
    salt = models.CharField(max_length=16) #unique identifier, used to generate filenames
    kind = models.CharField(max_length=5, choices=KIND_CHOICES)
    base_url = models.CharField(max_length=255, default="")

    owner = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "AssetBundle: {}".format(self.salt)

    def __unicode__(self):
        return "AssetBundle: {}".format(self.salt)

class Asset(models.Model):
    """ This is the Asset model """
    KIND_CHOICES = (
        ('original', 'Original'),
        ('large', 'Large'),
        ('small', 'Small'),
    )

    EXTENSION_CHOICES = (
        ('png', 'png'),
        ('gif', 'gif'),
        ('jpeg', 'jpg'),
        ('jpg', 'jpeg'),
    )

    asset_bundle = models.ForeignKey(AssetBundle)
    kind = models.CharField(max_length=8, choices=KIND_CHOICES, default="original")
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    extension = models.CharField(max_length=4, choices = EXTENSION_CHOICES)

    def __str__(self):
        return "Asset: {}: {}".format(self.asset_bundle.salt, self.kind)

    def __unicode__(self):
        return "Asset: {}: {}".format(self.asset_bundle.salt, self.kind)


class Item(models.Model):
    """ This is the model for items """

    asset_bundle = models.ForeignKey(AssetBundle)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank = True, null = True)
    price = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)

    owner = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    # @property
    # def full_title(self):
    #     if self.subtitle:
    #         return "{} - {}".format(self.title, self.subtitle)
    #     return self.title
    #
    # @property
    # def owner_email(self):
    #     return self.owner.email

    def __str__(self):
        return "Item: {}: {}".format(self.owner.username, self.asset_bundle.salt)

    def __unicode__(self):
        return "Item: {}: {}".format(self.owner.username, self.asset_bundle.salt)

class Comment(models.Model):
    """ This is the Comment model """
    item = models.ForeignKey(Item)
    body = models.TextField()

    owner = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Like(models.Model):
    """ This is the Like model """
    item = models.ForeignKey(Item)

    owner = models.ForeignKey(User, '')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)