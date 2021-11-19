from django.db.models import fields
from rest_framework import serializers
from watch_list.models import StreamPlatform, WatchList,Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model =Review
        exclude = ('watchlist',)
        # fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    reviews=ReviewSerializer(many=True,read_only=True)
    class Meta:
        model = WatchList
        fields ="__all__"

class StreamPlaformSerializer(serializers.ModelSerializer):
    watchlist=WatchListSerializer(many=True,read_only=True)
    class Meta:
        model = StreamPlatform
        fields ="__all__"
   