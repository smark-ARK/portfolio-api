# Generated by Django 4.1.5 on 2023-01-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("person", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="logo",
            field=models.CharField(max_length=500, null=True),
        ),
    ]