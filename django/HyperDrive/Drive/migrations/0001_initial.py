# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('pid', models.IntegerField(serialize=False, primary_key=True)),
                ('pname', models.CharField(default=None, max_length=200)),
                ('plat', models.FloatField(default=None)),
                ('plon', models.FloatField(default=None)),
                ('ptype', models.CharField(default=None, max_length=200)),
                ('ploc', models.CharField(default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('uid', models.IntegerField(default=1, serialize=False, primary_key=True)),
                ('uname', models.CharField(default=None, max_length=200)),
                ('upass', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserPlaces',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('placeid', models.ForeignKey(related_name='placeid', to='Drive.Places')),
                ('userid', models.ForeignKey(related_name='userid', to='Drive.UserInfo')),
            ],
        ),
    ]
