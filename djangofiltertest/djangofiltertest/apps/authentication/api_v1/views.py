from rest_framework.permissions import IsAuthenticated

from authentication.api_v1.serializers import UserSerializer
from authentication.models import User
from djangofiltertest.libs.views import APIListRetrieveUpdateViewSet


class UserViewSet(APIListRetrieveUpdateViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
