from rest_framework import serializers
from verify.models import PasscodeVerify


class PasscodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasscodeVerify
        fields = (
            'mobile',
            'passcode',
            'is_verified',
        )
