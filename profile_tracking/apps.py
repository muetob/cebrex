from django.apps import AppConfig


class ProfileTrackingConfig(AppConfig):
    name = 'profile_tracking'

    def ready(self):
        from profile_tracking import receivers
        from profile_tracking import backend