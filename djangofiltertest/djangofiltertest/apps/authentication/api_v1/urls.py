from rest_framework.routers import DefaultRouter

from authentication.api_v1.views import UserViewSet

# app_name = 'authentication'
router = DefaultRouter()
router.register(r'users', UserViewSet, base_name='authentication-user')

urlpatterns = router.urls
