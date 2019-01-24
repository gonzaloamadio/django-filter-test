from posts.api_v1.serializers import JobSerializer, ActiveJobSerializer
from posts.models import Job, ActiveJob
from djangofiltertest.libs.views import APIViewSet

from django_filters import rest_framework as filters


class ActiveJobFilter(filters.FilterSet):
    min_payment = filters.NumberFilter(field_name="number", lookup_expr="gte")
    max_payment = filters.NumberFilter(field_name="number", lookup_expr="lte")
    title = filters.CharFilter(lookup_expr='icontains')
    post_category = filters.CharFilter(lookup_expr='icontains', field_name='post_category__name')
    post_subcategory = filters.CharFilter(lookup_expr='icontains', field_name='post_subcategory__name')
    category = filters.CharFilter(lookup_expr='icontains', field_name='post_category__name')
    subcategory = filters.CharFilter(lookup_expr='icontains', field_name='post_subcategory__name')

    class Meta:
        model = ActiveJob
        fields = [
            "title",
            "post_category",
            "category",
            "subcategory",
            "post_subcategory",
            "min_payment",
            "max_payment",
        ]


class JobViewSet(APIViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = "slug"


class ActiveJobViewSet(APIViewSet):
    queryset = ActiveJob.objects.all()
    serializer_class = ActiveJobSerializer
    lookup_field = "slug"
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ActiveJobFilter
