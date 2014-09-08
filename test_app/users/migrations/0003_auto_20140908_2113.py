# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20140908_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='encrypted_password',
            field=models.CharField(max_length=255),
        ),
    ]
