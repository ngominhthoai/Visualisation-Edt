# Generated by Django 4.2 on 2023-05-22 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0033_part"),
    ]

    operations = [
        migrations.CreateModel(
            name="Classe",
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
                ("classename", models.CharField(max_length=255)),
                (
                    "edt",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.edt"
                    ),
                ),
                (
                    "part",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.part"
                    ),
                ),
            ],
        ),
    ]