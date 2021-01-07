from rest_framework import serializers
from .models import scrapdata

class scrapdataSerializers(serializers.ModelSerializer):
    class Meta:
        model = scrapdata
        fields = '__all__'