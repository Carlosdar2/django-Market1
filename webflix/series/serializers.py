from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.utils import serializer_helpers

from .models import Serie 



class SerieSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    release_date = serializers.DateField()
    rating = serializers.IntegerField()

def create(self,validated_data):
    return Serie.objects.create(**validated_data)

def update(self,instance,validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.release_date = validated_data.get('release_date', instance.release_date)
    instance.rating = validated_data.get('rating', instance.rating)
    instance.category = validated_data.get('category', instance.category)
    instance.save()
    return instance
class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ('id', 'name', 'release_date', 'rating', 'category')