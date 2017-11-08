from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets

from profiles.models import Profile
# Create your views here.
from profiles.serializers import ProfileSerializer


class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

