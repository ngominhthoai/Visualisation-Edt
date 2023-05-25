# Generated by Django 4.2 on 2023-05-22 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0028_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Teacher",
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
                ("teachername", models.CharField(max_length=255)),
                (
                    "edt",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.edt"
                    ),
                ),
            ],
        ),
    ]