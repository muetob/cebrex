from django.apps import apps
from django.conf import settings
from django.db.models.signals import post_save

from profile_tracking.backend import profile_tracking


def save_profile(sender, instance, created=False, **kwargs):
    if not created:
        profile_tracking.process_updated(instance)
    else:
        profile_tracking.process_created(instance)


post_save.connect(save_profile,
                  sender=apps.get_model(settings.PROFILE_TRACKING['PROFILE_MODEL']))