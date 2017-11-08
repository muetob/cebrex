from django.db import models

from core.models import CebrexModel
from core.models import CebrexManager


class ProfileManager(CebrexManager):
    def create_profile(self,
                       lastname,
                       firstname,
                       birthdate,
                       addresss):
        p = Profile(
            lastname=lastname,
            firstname=firstname,
            birthdate=birthdate,
            addresss=addresss
        )
        p.save()
        return p


class Profile(CebrexModel):
    lastname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    birthdate = models.DateField()

    address = models.ForeignKey('address.Address')

    objects = ProfileManager()