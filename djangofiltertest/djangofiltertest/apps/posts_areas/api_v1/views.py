from posts_areas.api_v1.serializers import PostAreaSerializer
from posts_areas.models import PostArea
from djangofiltertest.libs.views import APIViewSet


class PostAreaViewSet(APIViewSet):
    queryset = PostArea.objects.all()
    serializer_class = PostAreaSerializer
