from django.conf import settings
from django.db import models
from django.apps import apps

# Create your models here.
from core.models import CebrexModel


class ProfileSaveTracking(CebrexModel):
    profile = models.ForeignKey(
        settings.PROFILE_TRACKING['PROFILE_MODEL']
    )