from rest_framework import serializers
from zeno.models import ZenoItem

class ZenoItemSerializer(serializers.HyperlinkedModelSerializer):
  url = serializers.ReadOnlyField()
  class Meta:
    model = ZenoItem
    fields = ('zenoid', 'timestamp', 'temperature', 'duration', 'url')