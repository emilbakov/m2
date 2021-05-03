from rest_framework import serializers

from map.models import HuntingSpot


class HuntingSerializer(serializers.ModelSerializer):

    class Meta:
        model = HuntingSpot
        fields = (
            'id','title' , 'description' ,'picture', 'geom'
        )
        read_only_fields = ('id',)
        