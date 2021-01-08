from rest_framework import serializers
from .models import scrapdata


class scrapdataTitleSerializers(serializers.ModelSerializer):
    class Meta:
        model = scrapdata
        fields = ('title',)


class scrapdataRateingSerializers(serializers.ModelSerializer):
    class Meta:
        model = scrapdata
        fields = ('rating',)


class scrapdataReleaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = scrapdata
        fields = ('release_date',)


class scrapdataDurationSerializers(serializers.ModelSerializer):
    class Meta:
        model = scrapdata
        fields = ('duration',)


class scrapdataDescriptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = scrapdata
        fields = ('description',)


class scrapdataSerializers(serializers.ModelSerializer):
    class Meta:
        model = scrapdata
        fields = '__all__'
