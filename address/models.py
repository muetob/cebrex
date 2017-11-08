from django.db import models

from core.models import CebrexModel


class Address(CebrexModel):
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255)
    line3 = models.CharField(max_length=255)

    zip = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return '{} {} {}'.format(
            self.line1,
            self.zip,
            self.city
        )