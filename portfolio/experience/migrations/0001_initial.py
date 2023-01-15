# Generated by Django 4.1.5 on 2023-01-15 13:34

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("company_name", models.CharField(max_length=200)),
                ("website", models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="Experience",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("role", models.CharField(max_length=200)),
                ("level", models.CharField(max_length=300)),
                ("description", models.TextField()),
                (
                    "stack",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=100), size=None
                    ),
                ),
                (
                    "company_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="experience.company",
                    ),
                ),
            ],
        ),
    ]
