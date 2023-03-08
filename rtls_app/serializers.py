from rest_framework import serializers

from .models import *



class EnumerationTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EnumerationType
        fields = ('enum_type_id',
                  'description',
                  )

