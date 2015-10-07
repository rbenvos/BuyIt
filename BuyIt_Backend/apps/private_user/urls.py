from django.conf.urls import url, include
from apps.private_user.routers import PrivateUserRouter, PhoneRouter
from apps.private_user.views import PrivateUserViewSet, PhoneViewSet

router_users = PrivateUserRouter()
router_users.register(prefix='users',
                      viewset=PrivateUserViewSet,
                      base_name='private-user')

router_phones = PhoneRouter()
router_phones.register(prefix='users',
                       viewset=PhoneViewSet,
                       base_name='private-user')

urlpatterns = patterns = (
    url(r'', include(router_users.urls)),
    url(r'', include(router_phones.urls)),
)
