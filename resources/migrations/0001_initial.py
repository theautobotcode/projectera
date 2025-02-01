# Generated by Django 5.1.4 on 2025-01-30 06:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon_name', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submenus', to='resources.resource')),
            ],
            options={
                'db_table': 'resource',
            },
        ),
    ]
