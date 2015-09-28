from django.conf.urls import url, include
from apps.private_user.routers import PrivateUserRouter
from apps.private_user.views import PrivateUserViewSet

router = PrivateUserRouter()
router.register(prefix='users',
                viewset=PrivateUserViewSet,
                base_name='private-user')

urlpatterns = patterns = (
    url(r'', include(router.urls)),
)
