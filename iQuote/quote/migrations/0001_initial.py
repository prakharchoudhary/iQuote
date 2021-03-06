# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 11:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('quote', models.CharField(max_length=140)),
                ('category', models.CharField(choices=[(b'None', b'None'), (b'Happy', b'Happy'), (b'Sad', b'Sad'), (b'Inspiring', b'Inspiring'), (b'Romantic', b'Romantic'), (b'Sarcastic', b'Sarcastic'), (b'Funny', b'Funny'), (b'Evil', b'Evil'), (b'Bravery', b'Bravery'), (b'Wisdom', b'Wisdom')], default='Happy', max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
