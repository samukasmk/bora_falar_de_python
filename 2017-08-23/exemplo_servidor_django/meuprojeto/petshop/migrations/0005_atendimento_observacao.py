# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petshop', '0004_auto_20170804_0256'),
    ]

    operations = [
        migrations.AddField(
            model_name='atendimento',
            name='observacao',
            field=models.TextField(default=''),
        ),
    ]
