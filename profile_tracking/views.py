from rest_framework import generics

from profile_tracking.models import ProfileSaveTracking
# Create your views here.
from profile_tracking.serializers import ProfileSaveTrackingSerializer


class ProfileSaveTrackingListView(generics.ListCreateAPIView):
    queryset = ProfileSaveTracking.objects.all()
    serializer_class = ProfileSaveTrackingSerializer

