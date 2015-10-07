from rest_framework import serializers

from apps.private_user.models import PrivateUser, Friend, Phone


class PrivateUserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.CharField(required=True)
    password = serializers.CharField(max_length=200, required=False)
    name = serializers.CharField(max_length=200, required=True)
    last_name = serializers.CharField(max_length=200, required=True)
    active = serializers.BooleanField(default=True)

    class Meta:
        model = PrivateUser
        fields = ('id', 'email', 'name', 'last_name', 'active')
        read_only_fields = ('_get_device', '_get_friends', '_get_phones')
        write_only_fields = ('password',)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return PrivateUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('email', instance.title)
        instance.code = validated_data.get('name', instance.code)
        instance.linenos = validated_data.get('last_name', instance.linenos)
        instance.language = validated_data.get('active', instance.language)
        instance.style = validated_data.get('password', instance.style)
        instance.save()
        return instance


class PhoneSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=9, required=True)
    active = serializers.BooleanField(default=True)
