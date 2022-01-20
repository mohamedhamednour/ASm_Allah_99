from django.db import models

# Create your models here.

from embed_video.fields import EmbedVideoField


class Names(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=2000)
    Video = EmbedVideoField(null=True,blank=True)

    def __str__(self):
        return self.name


class Names_Allah(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=2000)
    Video = EmbedVideoField(null=True,blank=True)

    def __str__(self):
        return self.name
