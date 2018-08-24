# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-24 15:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0002_auto_20180824_0634'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cometario', models.TextField(verbose_name='Coment\xe1rio')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de cria\xe7\xe3o')),
                ('postId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Post')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usu\xe1rio')),
            ],
        ),
    ]