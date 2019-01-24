from rest_framework import serializers

from authentication import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        exclude = ('password',)
