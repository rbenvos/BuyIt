from django.conf.urls import url, include
from apps.device.routers import DeviceRouter
from apps.device.views import DeviceViewSet

router = DeviceRouter()
router.register(prefix='users',
                viewset=DeviceViewSet,
                base_name='private-user')

urlpatterns = patterns = (
    url(r'', include(router.urls)),
)

