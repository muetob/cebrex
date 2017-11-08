from rest_framework import generics

from profiles.models import Profile
# Create your views here.
from profiles.serializers import ProfileSerializer


class ProfileListView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

