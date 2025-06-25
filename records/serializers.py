from rest_framework import serializers
from .models import Player, Team, Record

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name', 'country']

class RecordSerializer(serializers.ModelSerializer):
    player = serializers.CharField(source='player.name')
    country = serializers.CharField(source='player.country.name')

    class Meta:
        model = Record
        fields = ['player', 'country', 'runs', 'wickets', 'is_not_out']
