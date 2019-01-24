from rest_framework.routers import DefaultRouter

from posts_areas.api_v1.views import PostAreaViewSet

# Create a router and register our viewsets with it.
# app_name = 'posts_areas'
router = DefaultRouter()
router.register(r'posts_areas', PostAreaViewSet, base_name="posts_areas-posts_areas")
urlpatterns = router.urls
