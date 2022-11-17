# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-11-17 05:02
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sender', '0003_auto_20221116_0754'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckedEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_name', models.CharField(max_length=254, verbose_name=b'\xd0\xa8\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xbe\xd0\xbd')),
                ('check_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd1\x82\xd0\xba\xd1\x80\xd1\x8b\xd1\x82\xd0\xb8\xd1\x8f')),
            ],
        ),
        migrations.AlterField(
            model_name='buyers',
            name='birth_date',
            field=models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x80\xd0\xbe\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='buyers',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='buyers',
            name='surname',
            field=models.CharField(max_length=100, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f'),
        ),
        migrations.AddField(
            model_name='buyers',
            name='checked',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buyer', to='sender.CheckedEmail'),
        ),
    ]