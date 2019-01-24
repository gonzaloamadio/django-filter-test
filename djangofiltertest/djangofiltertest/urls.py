from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers


# django rest framework router
router = routers.DefaultRouter()
# end of django rest framework router

api_v1 =[
    url(
        r'^api/v1/', include('djangofiltertest.apps.authentication.api_v1.urls')
    ),
    url(r'^api/v1/', include('djangofiltertest.apps.posts.api_v1.urls')),
    url(r'^api/v1/', include('djangofiltertest.apps.posts_areas.api_v1.urls')),
]

urlpatterns = [
    url(r'^', include(router.urls)),
#    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'', include((api_v1,'v1'), namespace="v1")),
]
