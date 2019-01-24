from rest_framework import serializers

from posts_areas.models import PostArea
from djangofiltertest.libs.serializers import AuditedModelSerializer


class PostAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostArea
        fields = '__all__'


class PostAreaSerializerAdmin(AuditedModelSerializer):
    class Meta:
        model = PostArea
        fields = '__all__'
