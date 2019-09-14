# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-14 22:17
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reproductivaApp', '0003_noticias'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContenidoSubCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateField()),
                ('categoriaPrincipal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reproductivaApp.CategoriaPostContenido')),
            ],
        ),
        migrations.CreateModel(
            name='PostContenidoSubCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('cuerpo', ckeditor.fields.RichTextField()),
                ('resumen', ckeditor.fields.RichTextField(null=True)),
                ('fecha_creacion', models.DateField()),
                ('imagen_portada', models.ImageField(null=True, upload_to='imagenes/')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reproductivaApp.Estado')),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reproductivaApp.CategoriaPostContenido')),
                ('usuario_creo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
