from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    """This is the model for items"""
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank = True, null = True)
    price = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)

    owner = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    @property
    def full_title(self):
        if self.subtitle:
            return "{} - {}".format(self.title, self.subtitle)
        return self.title

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
