# Generated by Django 4.2 on 2023-05-22 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0031_group"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("coursename", models.CharField(max_length=255)),
                (
                    "edt",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.edt"
                    ),
                ),
            ],
        ),
    ]
