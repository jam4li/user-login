# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class PasscodeVerify(models.Model):
    mobile = models.IntegerField(primary_key=True)
    passcode = models.CharField(max_length=4, default='0000')
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.mobile) + ',' + self.passcode
