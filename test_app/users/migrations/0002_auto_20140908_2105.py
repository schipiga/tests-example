# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(unique=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='encrypted_password',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
