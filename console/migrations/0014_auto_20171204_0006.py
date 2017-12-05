# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 23:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0013_auto_20171203_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='ark_send_to_second_address',
            field=models.IntegerField(choices=[(1, 'Send payout second address  .'), (2, 'Send payout to voting address  .')], default=2),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='inform_by_email',
            field=models.IntegerField(choices=[(1, "Don't inform me by email about payouts and current news       ."), (2, 'Feel free to send me emails  .')], default=1),
        ),
    ]
