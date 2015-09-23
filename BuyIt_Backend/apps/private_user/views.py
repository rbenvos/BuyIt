from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.private_user.models import PrivateUser
from apps.private_user.serializers import PrivateUserSerializer


class PrivateUserList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        private_users = PrivateUser.objects.all()
        serializer = PrivateUserSerializer(private_users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PrivateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)