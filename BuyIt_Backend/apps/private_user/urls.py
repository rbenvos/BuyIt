from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from apps.private_user.views import PrivateUserList

urlpatterns = [
    url(r'^users/$', PrivateUserList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
