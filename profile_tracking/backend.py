from django.conf import settings
from django.utils.module_loading import import_string


class ProfileTrackingBackend(object):
    def process_created(self, profile):
        pass

    def process_updated(self, profile):
        pass


class _ProfileTrackingBackends(object):
    def __init__(self):
        self._backends = None

    @property
    def backends(self):
        if self._backends is None:
            self._backends = []

            for be in settings.PROFILE_TRACKING_BACKENDS:
                be_class = import_string(be)

                self._backends.append(be_class())

        return self._backends


profile_tracking = _ProfileTrackingBackends()