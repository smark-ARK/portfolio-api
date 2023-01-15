# Generated by Django 4.1.5 on 2023-01-15 13:45

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Projects",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=300)),
                ("short_description", models.TextField()),
                (
                    "tech_used",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=200), size=None
                    ),
                ),
                ("detail_description", models.TextField()),
                ("github_link", models.CharField(max_length=300)),
                ("deploy_link", models.CharField(max_length=300)),
                (
                    "collaborators",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=200), size=None
                    ),
                ),
                ("video_explaination", models.CharField(max_length=300, null=True)),
                ("display_image", models.CharField(max_length=300, null=True)),
                (
                    "all_images",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=300), size=None
                    ),
                ),
            ],
        ),
    ]
