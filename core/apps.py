from importlib import import_module

from django.apps import AppConfig
from django.conf import settings

from logging import getLogger

logger = getLogger(__name__)


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        self._load_default_app_modules()

    # noinspection PyMethodMayBeStatic
    def _load_default_app_modules(self):
        for app in settings.INSTALLED_APPS:
            signals_module = '%s.signals' % app
            receivers_module = '%s.receivers' % app

            try:
                import_module(signals_module)
            except ImportError as e:
                logger.warning(
                    'failed to import "%s", reason: %s' % (signals_module, str(e)))
            try:
                import_module(receivers_module)
            except ImportError as e:
                logger.warning(
                    'failed to import "%s", reason: %s' % (receivers_module, str(e)))