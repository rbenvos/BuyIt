# Create your views here.
from io import BytesIO
from rest_framework import status
from rest_framework.decorators import detail_route
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from apps.device.models import Device
from apps.device.serializers import DeviceSerializer


class DeviceViewSet(ViewSet):
    """
    A viewset that provides the standard actions
    """

    def list(self, request, pk=None):
        devices = Device.objects.filter(user__pk=pk)
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)

    def perform_create(self, request, pk=None):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid:
            serializer.create(validated_data=serializer.initial_data)
            return Response(serializer.initial_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)