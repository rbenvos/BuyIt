from rest_framework import serializers
from apps.device.models import Device


class DeviceSerializer(serializers.Serializer):
    id_device = serializers.CharField(max_length=200, required=True)
    active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Device.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id_device = validated_data.get('id_device', instance.id_device)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance