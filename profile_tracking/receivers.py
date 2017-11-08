from profile_tracking import backend
from django.db.models.signals import post_save
from django.apps import apps
from django.conf import settings

from profile_tracking.backend import profile_tracking
from profile_tracking.models import ProfileSaveTracking


def save_profile(sender, instance, created=False, **kwargs):
    if not created:
        profile_tracking.process_updated(instance)
    else:
        profile_tracking.process_created(instance)


post_save.connect(save_profile,
                  sender=apps.get_model(settings.PROFILE_TRACKING['PROFILE_MODEL']))