from rest_framework import serializers

from profile_tracking.models import ProfileSaveTracking
from profiles.models import Profile


class ProfileSaveTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileSaveTracking
        fields = ['id',
                  'profile']