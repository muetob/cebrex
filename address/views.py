from rest_framework import generics

# Create your views here.

from address.models import Address
from address.serializers import AddressSerializer


class AddressListView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
