# Generated by Django 4.2 on 2023-05-10 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_rename_class_classe"),
    ]

    operations = [
        migrations.RenameField(
            model_name="groupclass",
            old_name="class_name",
            new_name="classe",
        ),
    ]
