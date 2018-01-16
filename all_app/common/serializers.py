from rest_framework import serializers

from .models import County, City, Province, File


class FileSerializer(serializers.HyperlinkedModelSerializer):
    file_path = serializers.SerializerMethodField(method_name='get_relative_path', read_only=True)

    def get_relative_path(self, val):
        return val.file

    class Meta:
        model = File
        fields = '__all__'


class ProvinceSerializer(serializers.ModelSerializer):
    level_name = serializers.CharField(source='level.name', read_only=True)

    class Meta:
        model = Province
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    level_name = serializers.CharField(source='level.name', read_only=True)

    class Meta:
        model = City
        fields = '__all__'


class CountySerializer(serializers.ModelSerializer):
    level_name = serializers.CharField(source='level.name', read_only=True)

    class Meta:
        model = County
        fields = '__all__'


