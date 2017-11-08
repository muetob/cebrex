from profile_tracking import backend
from django.db.models.signals import post_save
from django.apps import apps
from django.conf import settings

from profile_tracking.models import ProfileSaveTracking


def save_profile(sender, instance, **kwargs):
    pt = ProfileSaveTracking(
        profile=instance
    )

    pt.save()


post_save.connect(save_profile,
                  sender=apps.get_model(settings.PROFILE_TRACKING['PROFILE_MODEL']))