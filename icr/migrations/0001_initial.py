# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inwardcourierreistry',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('senders_code', models.CharField(max_length=10, null=True, blank=True)),
                ('senders_company', models.CharField(max_length=100, null=True, blank=True)),
                ('senders_address', models.CharField(max_length=3000, null=True, blank=True)),
                ('senders_city', models.CharField(max_length=3000, null=True, blank=True)),
                ('senders_name', models.CharField(max_length=3000, null=True, blank=True)),
                ('senders_phoneno', models.CharField(max_length=3000, null=True, blank=True)),
                ('senders_pincode', models.CharField(max_length=3000, null=True, blank=True)),
                ('senders_state', models.CharField(max_length=3000, null=True, blank=True)),
                ('senders_email', models.EmailField(max_length=254)),
                ('recivers_code', models.CharField(max_length=10, null=True, blank=True)),
                ('recivers_company', models.CharField(max_length=3000, null=True, blank=True)),
                ('recivers_address', models.CharField(max_length=3000, null=True, blank=True)),
                ('recivers_name', models.CharField(max_length=3000, null=True, blank=True)),
                ('recivers_phoneno', models.CharField(max_length=3000, null=True, blank=True)),
                ('recivers_pincode', models.CharField(max_length=3000, null=True, blank=True)),
                ('recivers_state', models.CharField(max_length=3000, null=True, blank=True)),
                ('recivers_email', models.EmailField(max_length=254)),
                ('special_instructions', models.CharField(max_length=8000, null=True, blank=True)),
                ('service_sticker', models.CharField(max_length=3000, null=True, blank=True)),
                ('original_senders_name', models.CharField(max_length=3000, null=True, blank=True)),
                ('courier_pickedup_by_name', models.CharField(max_length=3000, null=True, blank=True)),
                ('pickup_empid', models.CharField(max_length=3000, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('origin_of_the_courier', models.CharField(max_length=3000, null=True, blank=True)),
                ('destination_of_the_courier', models.CharField(max_length=3000, null=True, blank=True)),
                ('invoice_details', models.CharField(max_length=3000, null=True, blank=True)),
                ('invoice_value', models.CharField(max_length=3000, null=True, blank=True)),
                ('airway_bill_number', models.CharField(max_length=3000)),
                ('general_description', models.CharField(max_length=3000, null=True, blank=True)),
                ('number_of_packages', models.IntegerField()),
                ('gross_weight', models.IntegerField()),
                ('dimensonal_weight', models.IntegerField()),
            ],
        ),
    ]
