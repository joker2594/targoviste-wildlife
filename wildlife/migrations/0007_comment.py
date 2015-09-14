# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wildlife', '0006_auto_20150910_2342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField()),
                ('date_added', models.DateTimeField()),
                ('post', models.ForeignKey(to='wildlife.Post', null=True)),
                ('user_profile', models.ForeignKey(to='wildlife.UserProfile', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
