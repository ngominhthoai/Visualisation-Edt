# Generated by Django 4.2 on 2023-05-09 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="label",
            name="label",
        ),
    ]
