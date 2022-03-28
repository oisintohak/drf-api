from rest_framework import serializers
from .models import Like


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = [
            'owner', 'id', 'created_at', 'post'
        ]
