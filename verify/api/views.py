from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from rest_framework.response import Response

from verify.models import PasscodeVerify
from .serializers import PasscodeSerializer

from rest_framework.views import APIView

from rest_framework.permissions import AllowAny

from rest_framework import generics

from django.utils.translation import ugettext_lazy as _


class PasscodeVerify(APIView):
    def post(self, request, format=None):
        status = HTTP_400_BAD_REQUEST
        content = {}

        try:
            mobile = request.data.get('mobile').strip()
            passcode = request.data.get('passcode')
            is_verified = request.data.get('is_verified')

            content['msg'] = ""
            content['success'] = True

            status = HTTP_200_OK

            return Response(content, status=status)

        except:
            content['msg'] = _("Error")
            content['success'] = False
            return Response(content, status=status)
