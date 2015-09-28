from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from apps.private_user.models import PrivateUser
from apps.private_user.serializers import PrivateUserSerializer


class PrivateUserViewSet(ViewSet):
    """
    A viewset that provides the standard actions
    """

    def list(self, request, *args, **kwargs):
        queryset = PrivateUser.objects.all()
        serializer_class = PrivateUserSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        queryset = PrivateUser.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = PrivateUserSerializer(user)
        return Response(serializer.data)
