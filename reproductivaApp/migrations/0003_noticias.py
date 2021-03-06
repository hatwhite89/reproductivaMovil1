# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-14 20:37
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reproductivaApp', '0002_videos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('cuerpo', ckeditor.fields.RichTextField()),
                ('resumen', ckeditor.fields.RichTextField(null=True)),
                ('fecha_creacion', models.DateField()),
                ('imagen_portada', models.ImageField(null=True, upload_to='imagenes/')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reproductivaApp.Estado')),
                ('usuario_creo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
