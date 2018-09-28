# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-28 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PasscodeVerify',
            fields=[
                ('mobile', models.IntegerField(primary_key=True, serialize=False)),
                ('passcode', models.CharField(default='0000', max_length=4)),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
    ]