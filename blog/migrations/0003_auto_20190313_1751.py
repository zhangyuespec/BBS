# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190313_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comment_count',
            field=models.IntegerField(verbose_name='评论数', default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='down_count',
            field=models.IntegerField(verbose_name='踩数', default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='up_count',
            field=models.IntegerField(verbose_name='点赞数', default=0),
        ),
    ]
