# Generated by Django 5.0.7 on 2024-07-19 02:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='rememberTree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treeName', models.CharField(max_length=10)),
                ('myName', models.CharField(blank=True, max_length=100, null=True)),
                ('flowerType', models.CharField(max_length=20, null=True)),
                ('growth_period', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trees', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]