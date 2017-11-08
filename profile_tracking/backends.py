from profile_tracking.backend import ProfileTrackingBackend
from profile_tracking.models import ProfileSaveTracking


class ProfileTrackingDbEntryBackend(ProfileTrackingBackend):
    def process_created(self, profile):
        p = ProfileSaveTracking(
            profile=profile
        )
        p.save()

    def process_updated(self, profile):
        pt = ProfileSaveTracking.objects.get_for_profile(profile)
        pt.save()