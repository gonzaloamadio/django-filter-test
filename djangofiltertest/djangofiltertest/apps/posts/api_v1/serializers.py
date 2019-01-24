from rest_framework import serializers

from posts.models import Job, ActiveJob
from djangofiltertest.libs.serializers import AuditedModelSerializer


class JobSerializer(serializers.ModelSerializer):
    post_category = serializers.StringRelatedField()
    post_subcategory = serializers.StringRelatedField()
    class Meta:
        model = Job
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

class ActiveJobSerializer(serializers.ModelSerializer):
    post_category = serializers.StringRelatedField()
    post_subcategory = serializers.StringRelatedField()
    class Meta:
        model = ActiveJob
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

class JobSerializerAdmin(AuditedModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
