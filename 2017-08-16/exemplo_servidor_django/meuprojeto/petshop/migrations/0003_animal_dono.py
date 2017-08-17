# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petshop', '0002_dono'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='dono',
            field=models.ForeignKey(to='petshop.Dono', default=1),
        ),
    ]
