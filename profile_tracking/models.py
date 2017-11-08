from django.conf import settings
from django.db import models
from django.apps import apps

# Create your models here.
from core.models import CebrexModel
from core.models import CebrexManager


class ProfileTrackingManager(CebrexManager):
    def get_for_profile(self, profile):
        return self.filter(profile=profile)


class ProfileSaveTracking(CebrexModel):
    profile = models.ForeignKey(
        settings.PROFILE_TRACKING['PROFILE_MODEL']
    )

    objects = ProfileTrackingManager()