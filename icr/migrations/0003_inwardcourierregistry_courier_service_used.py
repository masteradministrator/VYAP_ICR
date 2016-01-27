# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('icr', '0002_auto_20160115_0520'),
    ]

    operations = [
        migrations.AddField(
            model_name='inwardcourierregistry',
            name='courier_service_used',
            field=models.CharField(max_length=3000, default=datetime.datetime(2016, 1, 15, 6, 15, 16, 661669, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
