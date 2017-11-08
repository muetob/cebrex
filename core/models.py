from django.db import models

# Create your models here.


class CebrexManager(models.Manager):
    pass


class CebrexModel(models.Model):
    objects = CebrexManager()

    class Meta:
        abstract=True