from django.conf.urls import url
from .views import PasscodeVerify

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'verify', PasscodeVerify.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
