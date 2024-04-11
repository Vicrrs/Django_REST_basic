# Generated by Django 5.0.4 on 2024-04-11 00:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('publicacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=False)),
                ('titulo', models.CharField(max_length=255)),
                ('url', models.URLField(unique=True)),
            ],
            options={
                'verbose_name': 'Cursor',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('publicacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=False)),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('comentario', models.TextField(blank=True, default='')),
                ('avaliacao', models.DecimalField(decimal_places=1,
                                                  max_digits=2)),
                ('curso', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                 related_name='avaliacoes', to='cursos.curso')),
            ],
            options={
                'verbose_name': 'Avaliações',
                'unique_together': {('email', 'curso')},
            },
        ),
    ]
