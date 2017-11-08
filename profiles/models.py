from django.db import models

from core.models import CebrexModel
from core.models import CebrexManager


class Profile(CebrexModel):
    lastname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    birthdate = models.DateField()

    address = models.ForeignKey('address.Address')