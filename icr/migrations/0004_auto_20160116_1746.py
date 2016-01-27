# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icr', '0003_inwardcourierregistry_courier_service_used'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inwardcourierregistry',
            options={'verbose_name_plural': 'InwardCourierRegistry'},
        ),
    ]
