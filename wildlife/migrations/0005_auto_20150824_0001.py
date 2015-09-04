# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wildlife', '0004_userprofile_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='user_profile',
            field=models.ForeignKey(to='wildlife.UserProfile', null=True),
            preserve_default=True,
        ),
    ]
