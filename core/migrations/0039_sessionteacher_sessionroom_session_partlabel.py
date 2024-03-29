# Generated by Django 4.2 on 2023-05-22 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0038_teacherlabel_roomlabel_courselabel"),
    ]

    operations = [
        migrations.CreateModel(
            name="SessionTeacher",
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
                ("rank", models.IntegerField()),
                (
                    "classe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.classe"
                    ),
                ),
                (
                    "edt",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.edt"
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.teacher"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SessionRoom",
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
                ("rank", models.IntegerField()),
                (
                    "classe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.classe"
                    ),
                ),
                (
                    "edt",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.edt"
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.room"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Session",
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
                ("rank", models.IntegerField()),
                ("daily_slot", models.IntegerField()),
                ("day", models.IntegerField()),
                ("week", models.IntegerField()),
                (
                    "classe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.classe"
                    ),
                ),
                (
                    "edt",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.edt"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PartLabel",
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
                (
                    "edt",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.edt"
                    ),
                ),
                (
                    "label",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.label"
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
