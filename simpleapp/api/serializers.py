from rest_framework import serializers

from ..models import Simple


class SimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Simple
        fields = ['title', 'slug', 'point']
