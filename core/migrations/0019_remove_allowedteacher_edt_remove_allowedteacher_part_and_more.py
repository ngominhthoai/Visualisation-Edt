# Generated by Django 4.2 on 2023-05-16 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0018_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="allowedteacher",
            name="edt",
        ),
        migrations.RemoveField(
            model_name="allowedteacher",
            name="part",
        ),
        migrations.RemoveField(
            model_name="allowedteacher",
            name="teacher",
        ),
        migrations.RemoveField(
            model_name="classe",
            name="edt",
        ),
        migrations.RemoveField(
            model_name="classe",
            name="part",
        ),
        migrations.RemoveField(
            model_name="course",
            name="edt",
        ),
        migrations.RemoveField(
            model_name="courselabel",
            name="course",
        ),
        migrations.RemoveField(
            model_name="courselabel",
            name="edt",
        ),
        migrations.RemoveField(
            model_name="courselabel",
            name="label",
        ),
        migrations.RemoveField(
            model_name="edt",
            name="user",
        ),
        migrations.RemoveField(
            model_name="group",
            name="edt",
        ),
        migrations.RemoveField(
            model_name="groupclass",
            name="classe",
        ),
        migrations.RemoveField(
            model_name="groupclass",
            name="edt",
        ),
        migrations.RemoveField(
            model_name="groupclass",
            name="group",
        ),
        migrations.RemoveField(
            model_name="label",
            name="edt",
        ),
        migrations.RemoveField(
            model_name="part",
            name="course",
        ),
        migrations.RemoveField(
            model_name="part",
            name="edt",
        ),
        migrations.RemoveField(
            model_name="partlabel",
            name="edt",
        ),
        migrations.RemoveField(
            model_name="partlabel",
            name="label",
        ),
        migrations.RemoveField(
            model_name="partlabel",
            name="part",
        ),
        migrations.RemoveField(
            model_name="room",
            name="edt",
        ),
        migrations.RemoveField(
            model_name="roomlabel",
            name="edt",
        ),
        migrations.RemoveField(
            model_name="roomlabel",
            name="label",
        ),
        migrations.RemoveField(
            model_name="roomlabel",
            name="room",
        ),
        migrations.RemoveField(
            model_name="session",
            name="classe",
        ),
        migrations.RemoveField(
            model_name="session",
            name="edt",
        ),
        migrations.RemoveField(
            model_name="sessionroom",
            name="classe",
        ),
        migrations.RemoveField(
            model_name="sessionroom",
            name="edt",
        ),
        migrations.RemoveField(
            model_name="sessionroom",
            name="room",
        ),
        migrations.RemoveField(
            model_name="sessionteacher",
            name="classe",
        ),
        migrations.RemoveField(
            model_name="sessionteacher",
            name="edt",
        ),
        migrations.RemoveField(
            model_name="sessionteacher",
            name="teacher",
        ),
        migrations.RemoveField(
            model_name="teacher",
            name="edt",
        ),
        migrations.RemoveField(
            model_name="teacherlabel",
            name="edt",
        ),
        migrations.RemoveField(
            model_name="teacherlabel",
            name="label",
        ),
        migrations.RemoveField(
            model_name="teacherlabel",
            name="teacher",
        ),
        migrations.DeleteModel(
            name="AllowedRoom",
        ),
        migrations.DeleteModel(
            name="AllowedTeacher",
        ),
        migrations.DeleteModel(
            name="Classe",
        ),
        migrations.DeleteModel(
            name="Course",
        ),
        migrations.DeleteModel(
            name="CourseLabel",
        ),
        migrations.DeleteModel(
            name="Edt",
        ),
        migrations.DeleteModel(
            name="Group",
        ),
        migrations.DeleteModel(
            name="GroupClass",
        ),
        migrations.DeleteModel(
            name="Label",
        ),
        migrations.DeleteModel(
            name="Part",
        ),
        migrations.DeleteModel(
            name="PartLabel",
        ),
        migrations.DeleteModel(
            name="Room",
        ),
        migrations.DeleteModel(
            name="RoomLabel",
        ),
        migrations.DeleteModel(
            name="Session",
        ),
        migrations.DeleteModel(
            name="SessionRoom",
        ),
        migrations.DeleteModel(
            name="SessionTeacher",
        ),
        migrations.DeleteModel(
            name="Teacher",
        ),
        migrations.DeleteModel(
            name="TeacherLabel",
        ),
    ]
