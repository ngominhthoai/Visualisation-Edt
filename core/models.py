from django.db import models
from django.conf import settings


class Edt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Label(models.Model):
    labelname = models.CharField(max_length=255)
    edt = models.ForeignKey(Edt, on_delete=models.CASCADE)

class Teacher(models.Model):
    teachername = models.CharField(max_length=255)
    edt = models.ForeignKey(Edt, on_delete=models.CASCADE)

class Room(models.Model):
    roomname = models.CharField(max_length=255)
    capacity = models.IntegerField(null=True)
    edt = models.ForeignKey(Edt, on_delete=models.CASCADE)

class Group(models.Model):
    groupname = models.CharField(max_length=255)
    headCount = models.IntegerField()
    edt = models.ForeignKey(Edt, on_delete=models.CASCADE)

class Course(models.Model):
    coursename = models.CharField(max_length=255)
    edt = models.ForeignKey(Edt, on_delete=models.CASCADE)


class Part(models.Model):
    partname = models.CharField(max_length=255)
    nrSessions = models.IntegerField()
    maxHeadCount = models.IntegerField()
    sessionLength = models.IntegerField()
    dailySlots = models.CharField(max_length=255)
    days = models.CharField(max_length=255)
    weeks = models.CharField(max_length=255)
    sessionRooms = models.CharField(max_length=255, null=True, blank=True, default=None)
    sessionTeachers = models.CharField(max_length=255, null=True, blank=True, default=None)
    course = models.ForeignKey(Course, on_delete=models.CASCADE) #sur le coursename
    edt = models.ForeignKey(Edt, on_delete=models.CASCADE)


class Classe(models.Model):
    classename = models.CharField(max_length=255)
    part = models.ForeignKey(Part, on_delete=models.CASCADE) #sur le partname
    edt = models.ForeignKey(Edt, on_delete=models.CASCADE)

class AllowedRoom(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    edt = models.ForeignKey(Edt, on_delete=models.CASCADE)

class AllowedTeacher(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    edt = models.ForeignKey(Edt, on_delete=models.CASCADE)

class GroupClass(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, null=True, blank=True, default=None)
    edt = models.ForeignKey(Edt, on_delete=models.CASCADE)

class RoomLabel(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #sur le roomname
    label = models.ForeignKey(Label, on_delete=models.CASCADE) #sur le labelname
    edt = models.ForeignKey(Edt, on_delete=models.CASCADE)

class CourseLabel(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    edt = models.ForeignKey(Edt, on_delete=models.CASCADE)


class TeacherLabel(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    edt = models.ForeignKey(Edt, on_delete=models.CASCADE)

class PartLabel(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    edt = models.ForeignKey(Edt, on_delete=models.CASCADE)

class Session(models.Model):
    rank = models.IntegerField()
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    daily_slot = models.IntegerField()
    day = models.IntegerField()
    week = models.IntegerField()
    edt = models.ForeignKey(Edt, on_delete=models.CASCADE)

class SessionTeacher(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    rank = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    edt = models.ForeignKey(Edt, on_delete=models.CASCADE)


class SessionRoom(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    rank = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    edt = models.ForeignKey(Edt, on_delete=models.CASCADE)
