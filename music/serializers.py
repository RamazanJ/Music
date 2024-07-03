from rest_framework import serializers
from .models import Song

class MusicFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name', 'file']
