from rest_framework import serializers

from address.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id',
                  'line1',
                  'line2',
                  'line3',
                  'zip',
                  'city']