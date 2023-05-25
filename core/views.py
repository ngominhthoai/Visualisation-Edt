from datetime import datetime, timedelta, timezone

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from core.models import *


# Create your views here.
@login_required
# def home(request):
#     return render(request, 'core/home2.html')
def home(request):
    return render(request, 'calendar.html')


def chargerXml(request):
    return render(request, 'core/chargerXml.html')

from django.shortcuts import render, redirect


import xml.etree.ElementTree as ET

def create_objects_from_xml(request):
    if request.method == 'POST':
        xml_file = request.FILES.get('xml-file')
        tree = ET.parse(xml_file)
        root = tree.getroot()

        #creer Edt object
        edt = Edt(user=request.user)
        edt.save()

        # last edt
        edt_id = Edt.objects.last()

        # ----------------------------------------------

        # labels dans les rooms: room[@id and @label]
        for room in root.findall('.//rooms/room[@id][@label]'):
            label_room = room.get('label')
            Label.objects.get_or_create(labelname=label_room, edt=edt_id)

        # labels dans les teachers
        for teacher in root.findall('.//teachers/teacher[@id][@label]'):
            label_teacher = teacher.get('label')
            Label.objects.get_or_create(labelname=label_teacher, edt=edt_id)

        # labels dans les courses
        for course in root.findall('.//courses/course[@id][@label]'):
            label_course = course.get('label')
            Label.objects.get_or_create(labelname=label_course, edt=edt_id)
            for part in course.findall('.//part[@id][@label]'):
                label_part = part.get('label')
                Label.objects.get_or_create(labelname=label_part, edt=edt_id)

        # tous les teachers dans les teachers
        for teacher in root.findall('.//teachers/teacher[@id]'):
            teacher_name = teacher.get('id')
            Teacher.objects.get_or_create(teachername=teacher_name, edt=edt_id)

        # tous les rooms
        for room in root.findall('.//rooms/room[@id]'):
            room_name = room.get('id')
            room_capacity = room.get('capacity')
            Room.objects.get_or_create(roomname=room_name, capacity=room_capacity, edt=edt_id)

        # tous les groups
        for group in root.findall('.//groups/group[@id]'):
            group_name = group.get('id')
            group_headCount = group.get('headCount')
            Group.objects.get_or_create(groupname=group_name, headCount=group_headCount, edt=edt_id)

        # tous les courses
        for course in root.findall('.//courses/course[@id]'):
            course_name = course.get('id')
            Course.objects.get_or_create(coursename=course_name, edt=edt_id)

        # # tous les parts
        for course in root.findall('.//courses/course'):
            for part in course.findall('.//part'):
                part_name = part.get('id')
                part_nrSessions = part.get('nrSessions')
                part_maxHeadCount = part.find('.//classes').get('maxHeadCount')
                part_sessionLength = part.find('.//allowedSlots').get('sessionLength')
                part_dailySlots = part.find('.//allowedSlots/dailySlots').text
                part_days = part.find('.//allowedSlots/days').text
                part_weeks = part.find('.//allowedSlots/weeks').text
                if part.find('.//allowedRooms') is None:
                    part_sessionRooms = None
                else:
                    part_sessionRooms = part.find('.//allowedRooms').get('sessionRooms')
                if part.find('.//allowedTeachers') is None:
                    part_sessionTeachers = None
                else:
                    part_sessionTeachers = part.find('.//allowedTeachers').get('sessionTeachers')
                part_course = Course.objects.get(coursename=course.get('id'), edt=edt_id)
                Part.objects.get_or_create(partname=part_name, nrSessions=part_nrSessions, maxHeadCount=part_maxHeadCount,
                                             sessionLength=part_sessionLength, dailySlots=part_dailySlots, days=part_days,
                                                weeks=part_weeks, sessionRooms=part_sessionRooms, sessionTeachers=part_sessionTeachers,
                                                    course=part_course, edt=edt_id)
                #table classe
                for classe in part.findall('.//classes/class'):
                    part = Part.objects.get(partname=part_name, edt=edt_id)
                    classe_name = classe.get('id')
                    Classe.objects.get_or_create(classename=classe_name, part=part, edt=edt_id)

        # table allowedroom
        for course in root.findall('.//courses/course'):
            for part in course.findall('.//part'):
                part_id = part.get('id')

                if part.find('.//allowedRooms') is None:
                    pass
                else:
                    for allowedRoom in part.findall('.//allowedRooms/room'):
                        room_id = allowedRoom.get('refId')
                        room = Room.objects.get(roomname=room_id, edt=edt_id)
                        part = Part.objects.get(partname=part_id, edt=edt_id)
                        AllowedRoom.objects.get_or_create(room=room, part=part, edt=edt_id)


        # table allowedteacher
        for course in root.findall('.//courses/course'):
            for part in course.findall('.//part'):
                part_id = part.get('id')
                if part.find('.//allowedTeachers') is None:
                    pass
                else:
                    for allowedTeacher in part.findall('.//allowedTeachers/teacher'):
                        teacher_id = allowedTeacher.get('refId')
                        teacher = Teacher.objects.get(teachername=teacher_id, edt=edt_id)
                        part = Part.objects.get(partname=part_id, edt=edt_id)
                        AllowedTeacher.objects.get_or_create(teacher=teacher, part=part, edt=edt_id)


        # # table groupclass
        for group in root.findall('.//groups/group'):
            group_id = group.get('id')
            for groupClass in group.findall('.//classes/class'):
                groupClass_id = groupClass.get('refId')
                group = Group.objects.get(groupname=group_id, edt=edt_id)
                classe = Classe.objects.get(classename=groupClass_id, edt=edt_id)
                GroupClass.objects.get_or_create(group=group, classe=classe, edt=edt_id)

        # table RoomLabel
        for room in root.findall('.//rooms/room[@id][@label]'):
            room_id = room.get('id')
            room_label_id = room.get('label')
            room = Room.objects.get(roomname=room_id, edt=edt_id)
            label = Label.objects.get(labelname=room_label_id, edt=edt_id)
            RoomLabel.objects.get_or_create(room=room, label=label, edt=edt_id)

        # table CourseLabel
        for course in root.findall('.//courses/course'):
            course_id = course.get('id')
            course_label_id = course.get('label')
            course = Course.objects.get(coursename=course_id, edt=edt_id)
            label = Label.objects.get(labelname=course_label_id, edt=edt_id)
            CourseLabel.objects.get_or_create(course=course, label=label, edt=edt_id)

        # table TeacherLabel(models.Model):
        for teacher in root.findall('.//teachers/teacher[@id][@label]'):
            teacher_id = teacher.get('id')
            teacher_label_id = teacher.get('label')
            teacher = Teacher.objects.get(teachername=teacher_id, edt=edt_id)
            label = Label.objects.get(labelname=teacher_label_id, edt=edt_id)
            TeacherLabel.objects.get_or_create(teacher=teacher, label=label, edt=edt_id)

        # table PartLabel(models.Model):
        for course in root.findall('.//courses/course'):
            for part in course.findall('.//part'):
                part_id = part.get('id')
                part_label_id = part.get('label')
                part = Part.objects.get(partname=part_id, edt=edt_id)
                label = Label.objects.get(labelname=part_label_id, edt=edt_id)
                PartLabel.objects.get_or_create(part=part, label=label, edt=edt_id)

        # table session
        for session in root.findall('.//solution/sessions/session'):
            session_rank = session.get('rank')
            session_classe_id = session.get('class')
            session_daily_slot = session.find('.//startingSlot').get('dailySlot')
            session_day = session.find('.//startingSlot').get('day')
            session_week = session.find('.//startingSlot').get('week')
            classe = Classe.objects.get(classename=session_classe_id, edt=edt_id)
            Session.objects.get_or_create(rank=session_rank, classe=classe, daily_slot=session_daily_slot,
                                          day=session_day, week=session_week, edt=edt_id)
        #table sessionteacher
        for session in root.findall('.//solution/sessions/session'):
            session_rank = session.get('rank')
            session_classe_id = session.get('class')
            classe = Classe.objects.get(classename=session_classe_id, edt=edt_id)
            for teacher in session.findall('.//teachers/teacher[@refId]'):
                teacher_id = teacher.get('refId')
                teacher = Teacher.objects.get(teachername=teacher_id, edt=edt_id)
                SessionTeacher.objects.get_or_create(rank=session_rank, classe=classe, teacher=teacher, edt=edt)

        # table sessionroom
        for session in root.findall('.//solution/sessions/session'):
            session_rank = session.get('rank')
            session_classe_id = session.get('class')
            classe = Classe.objects.get(classename=session_classe_id, edt=edt_id)
            for room in session.findall('.//rooms/room[@refId]'):
                room_id = room.get('refId')
                room = Room.objects.get(roomname=room_id, edt=edt_id)
                SessionRoom.objects.get_or_create(rank=session_rank, classe=classe, room=room, edt=edt)

    return HttpResponse('ok')

def load_events(request):
    # start_date = request.GET.get('start')  # Get the start date from the request
    # end_date = request.GET.get('end')  # Get the end date from the request
    # edt_id = request.POST.get('edt_id')
    # date_start = request.POST.get('date')
    # # if date_start is null, date_start = today
    # if date_start is None:
    #     date_start = datetime.now()
    # else:
    #     date_start = datetime.strptime(date_start, '%Y-%m-%d')
    #
    # print(date_start)
    edt_id = Edt.objects.get(id=41)
    events = []
    sessions = Session.objects.filter(edt=edt_id)

    for session in sessions:
        duration = session.classe.part.sessionLength
        nbr_session = session.classe.part.nrSessions

        category_colors = {
            'CC': 'blue',
            'CT': 'red',
            'EVAL,CC': 'green',
            'TP': 'orange',
            'CM': 'purple',
            'TD': 'yellow',
            'CTD': 'pink',
            'REPAS': 'brown',
            'Virtuelle': 'gray',
            'CM,TD': 'teal'
        }

        # category
        try:
            part_labels = PartLabel.objects.select_related('label').filter(part=session.classe.part, edt=edt_id)
            label_names = [part_label.label.labelname for part_label in part_labels]
        except PartLabel.DoesNotExist:
            label_names = None

        colors = [category_colors.get(category, 'gray') for category in label_names]

        # room
        try:
            session_rooms = SessionRoom.objects.select_related('room').filter(classe=session.classe, rank=session.rank,
                                                                              edt=edt_id)
            room_names = [session_room.room.roomname for session_room in session_rooms]
        except SessionRoom.DoesNotExist:
            room_names = None

        #capacite de la salle( room capacity)
        try:
            session_rooms = SessionRoom.objects.select_related('room').filter(classe=session.classe, rank=session.rank,
                                                                              edt=edt_id)
            room_capacity = [session_room.room.capacity for session_room in session_rooms]
        except SessionRoom.DoesNotExist:
            room_capacity = None

        # teacher
        try:
            session_teachers = SessionTeacher.objects.select_related('teacher').filter(classe=session.classe, rank=session.rank,
                                                                              edt=edt_id)
            teacher_names = [session_teacher.teacher.teachername for session_teacher in session_teachers]
        except SessionTeacher.DoesNotExist:
            teacher_names = None


        # (room disponibilities)
        try:
            allowed_rooms = AllowedRoom.objects.filter(part=session.classe.part, edt=edt_id)
            room_disponibilities = [allowed_room.room.roomname for allowed_room in allowed_rooms]
        except AllowedRoom.DoesNotExist:
            room_disponibilities = None

        # (teacher disponibilities)
        try:
            allowed_teachers = AllowedTeacher.objects.filter(part=session.classe.part, edt=edt_id)
            teacher_disponibilities = [allowed_teacher.teacher.teachername for allowed_teacher in allowed_teachers]
        except AllowedTeacher.DoesNotExist:
            teacher_disponibilities = None

        # horraire disponibilities
        part = session.classe.part
        slots = part.dailySlots.split(',')  # convert dailySlots to list

        time_grid = []
        for slot in slots:
            if '-' in slot:  # traite les slots contenant un tiret
                start, end = slot.split('-')
                start = int(start)
                end = int(end)
                time_grid.extend(list(range(start, end + 1)))  # ajoute les slots dans l'intervalle
            else:
                time_grid.append(int(slot))  # ajoute le slot simple

        # convertir les slots en hh:mm
        time_slots = []
        for slot in time_grid:
            hour = (slot // 60)  # la partie entière est l'heure
            minute = (slot % 60)  # le reste est les minutes
            time_slots.append(f"{hour:02d}:{minute:02d}")  # convertir en hh:mm


        start_time = datetime(2023, 1, 1) + timedelta(weeks=session.week, days=session.day, minutes=session.daily_slot)
        end_time = start_time + timedelta(minutes=duration)

        event = {
            'title': session.classe.classename,
            'start': start_time.isoformat(),
            'end': end_time.isoformat(),
            'color': colors[0],  #utiliser la première couleur de la liste des couleurs
            'extendedProps': {
                'duration': duration,
                'nbr_session': nbr_session,
                'capacity': room_capacity,
                'teacher': teacher_names,
                'room': room_names,
                'category': label_names,
                # 'roomdisponibilities': room_disponibilities,
                # 'teacherdisponibilities': teacher_disponibilities,
                # 'horrairedisponibilities': time_slots,
            },
        }

        events.append(event)
    return JsonResponse(events, safe=False)


# retourne les events d'un edt sous forme d'une liste de dictionnaires
def load_events1(request):
    edt= Edt.objects.get(id=41)
    sessions = Session.objects.filter(edt=edt)
    session_list = []
    salle_list = []
    prof_list = []
    category_list = []
    matiere_list = []

    for session in sessions:
        duration = session.classe.part.sessionLength
        nbr_session = session.classe.part.nrSessions

        category_colors = {
            'CC': 'blue',
            'CT': 'red',
            'EVAL,CC': 'green',
            'TP': 'orange',
            'CM': 'purple',
            'TD': 'yellow',
            'CTD': 'pink',
            'REPAS': 'brown',
            'Virtuelle': 'gray',
            'CM,TD': 'teal'
        }

        #category
        try:
            part_labels = PartLabel.objects.select_related('label').filter(part=session.classe.part, edt=edt)
            label_names = [part_label.label.labelname for part_label in part_labels]
            # add category to list with id and name
            for category in label_names:
                if category not in category_list:
                    category_list.append(category)
        except PartLabel.DoesNotExist:
            label_names = None


        colors = [category_colors.get(category, 'gray') for category in label_names]

        # room
        try:
            session_rooms = SessionRoom.objects.select_related('room').filter(classe=session.classe, rank=session.rank,
                                                                              edt=edt)
            room_names = [session_room.room.roomname for session_room in session_rooms]
        #   add room to list
        #     salle_list.append(room_names)
            for room in room_names:
                if room not in salle_list:
                    salle_list.append(room)
        except SessionRoom.DoesNotExist:
            room_names = None

        #capacite de la salle( room capacity)
        try:
            session_rooms = SessionRoom.objects.select_related('room').filter(classe=session.classe, rank=session.rank,
                                                                              edt=edt)
            room_capacity = [session_room.room.capacity for session_room in session_rooms]
        except SessionRoom.DoesNotExist:
            room_capacity = None

        # teacher
        try:
            session_teachers = SessionTeacher.objects.select_related('teacher').filter(classe=session.classe, rank=session.rank,
                                                                              edt=edt)
            teacher_names = [session_teacher.teacher.teachername for session_teacher in session_teachers]
            #add teacher to list with id and name
            for teacher in teacher_names:
                if teacher not in prof_list:
                    prof_list.append(teacher)
        except SessionTeacher.DoesNotExist:
            teacher_names = None


        # (room disponibilities)
        try:
            allowed_rooms = AllowedRoom.objects.filter(part=session.classe.part, edt=edt)
            room_disponibilities = [allowed_room.room.roomname for allowed_room in allowed_rooms]
        except AllowedRoom.DoesNotExist:
            room_disponibilities = None

        # (teacher disponibilities)
        try:
            allowed_teachers = AllowedTeacher.objects.filter(part=session.classe.part, edt=edt)
            teacher_disponibilities = [allowed_teacher.teacher.teachername for allowed_teacher in allowed_teachers]
        except AllowedTeacher.DoesNotExist:
            teacher_disponibilities = None

        # horraire disponibilities
        part = session.classe.part
        slots = part.dailySlots.split(',')  # change dailyslots to list

        time_grid = []
        for slot in slots:
            if '-' in slot:  # traitement du cas ou il y a un tiret
                start, end = slot.split('-')
                start = int(start)
                end = int(end)
                time_grid.extend(list(range(start, end + 1)))  # ajouter la liste des slots de start à end
            else:
                time_grid.append(int(slot))  # ajouter le slot seul

        # convertir de slot à heure et minute
        time_slots = []
        for slot in time_grid:
            hour = (slot // 60)  # la partie entière est l'heure
            minute = (slot % 60)  # la partie décimale est les minutes
            time_slots.append(f"{hour:02d}:{minute:02d}")  # formater l'heure et les minutes en chaîne hh:mm

        start_time = datetime(2023, 1, 1) + timedelta(weeks=session.week, days=session.day, minutes=session.daily_slot)
        end_time = start_time + timedelta(minutes=duration)


        session_dict = {
            'title': session.classe.classename,
            'start': start_time.isoformat(),
            'end': end_time.isoformat(),
            'color': colors[0],  # utiliser la première couleur de la liste des couleurs
            'extendedProps': {
                'duration': duration,
                'nbr_session': nbr_session,
                'capacity': room_capacity,
                'teacher': teacher_names,
                'room': room_names,
                'category': label_names,
                'roomdisponibilities': room_disponibilities,
                'teacherdisponibilities': teacher_disponibilities,
                'horrairedisponibilities': time_slots,
            },
        }

        #add matiere to list with id and name
        if session.classe.classename not in matiere_list:
            matiere_list.append(session.classe.classename)

        session_list.append(session_dict)

        # tri par ordre alphabetique des listes
        salle_list.sort()
        prof_list.sort()
        category_list.sort()
        matiere_list.sort()

    context = {
        'sessions': session_list,
        'salles': salle_list,
        'profs': prof_list,
        'categories': category_list,
        'matieres': matiere_list,
    }

    return render(request, 'core/home.html', context)


def edt_list(request):
    edts = Edt.objects.filter(user=request.user)
    context = {
        'edts': edts
    }
    return render(request, 'core/edt_list.html', context)

def home2(request):
    return render(request, 'core/calendar2.html')

def load_events2(request):
    # start_date = request.GET.get('start')  # Get the start date from the request
    # end_date = request.GET.get('end')  # Get the end date from the request
    edt_id = request.POST.get('edt_id')
    date_start = request.POST.get('date')
    # if date_start is null, date_start = today
    if date_start is None:
        date_start = datetime.now()
    else:
        date_start = datetime.strptime(date_start, '%Y-%m-%d')
    #
    # print(date_start)
    # edt_id = Edt.objects.get(id=41)
    events = []
    sessions = Session.objects.filter(edt=edt_id)

    for session in sessions:
        duration = session.classe.part.sessionLength
        nbr_session = session.classe.part.nrSessions

        category_colors = {
            'CC': 'blue',
            'CT': 'red',
            'EVAL,CC': 'green',
            'TP': 'orange',
            'CM': 'purple',
            'TD': 'yellow',
            'CTD': 'pink',
            'REPAS': 'brown',
            'Virtuelle': 'gray',
            'CM,TD': 'teal'
        }

        # category
        try:
            part_labels = PartLabel.objects.select_related('label').filter(part=session.classe.part, edt=edt_id)
            label_names = [part_label.label.labelname for part_label in part_labels]
        except PartLabel.DoesNotExist:
            label_names = None

        colors = [category_colors.get(category, 'gray') for category in label_names]

        # room
        try:
            session_rooms = SessionRoom.objects.select_related('room').filter(classe=session.classe, rank=session.rank,
                                                                              edt=edt_id)
            room_names = [session_room.room.roomname for session_room in session_rooms]
        except SessionRoom.DoesNotExist:
            room_names = None

        #capacite de la salle( room capacity)
        try:
            session_rooms = SessionRoom.objects.select_related('room').filter(classe=session.classe, rank=session.rank,
                                                                              edt=edt_id)
            room_capacity = [session_room.room.capacity for session_room in session_rooms]
        except SessionRoom.DoesNotExist:
            room_capacity = None

        # teacher
        try:
            session_teachers = SessionTeacher.objects.select_related('teacher').filter(classe=session.classe, rank=session.rank,
                                                                              edt=edt_id)
            teacher_names = [session_teacher.teacher.teachername for session_teacher in session_teachers]
        except SessionTeacher.DoesNotExist:
            teacher_names = None


        # (room disponibilities)
        try:
            allowed_rooms = AllowedRoom.objects.filter(part=session.classe.part, edt=edt_id)
            room_disponibilities = [allowed_room.room.roomname for allowed_room in allowed_rooms]
        except AllowedRoom.DoesNotExist:
            room_disponibilities = None

        # (teacher disponibilities)
        try:
            allowed_teachers = AllowedTeacher.objects.filter(part=session.classe.part, edt=edt_id)
            teacher_disponibilities = [allowed_teacher.teacher.teachername for allowed_teacher in allowed_teachers]
        except AllowedTeacher.DoesNotExist:
            teacher_disponibilities = None

        # horraire disponibilities
        part = session.classe.part
        slots = part.dailySlots.split(',')  # convert dailySlots to list

        time_grid = []
        for slot in slots:
            if '-' in slot:  # traite les slots contenant un tiret
                start, end = slot.split('-')
                start = int(start)
                end = int(end)
                time_grid.extend(list(range(start, end + 1)))  # ajoute les slots dans l'intervalle
            else:
                time_grid.append(int(slot))  # ajoute le slot simple

        # convertir les slots en hh:mm
        time_slots = []
        for slot in time_grid:
            hour = (slot // 60)  # la partie entière est l'heure
            minute = (slot % 60)  # le reste est les minutes
            time_slots.append(f"{hour:02d}:{minute:02d}")  # convertir en hh:mm


        start_time = date_start + timedelta(weeks=session.week, days=session.day, minutes=session.daily_slot)
        end_time = start_time + timedelta(minutes=duration)

        event = {
            'title': session.classe.classename,
            'start': start_time.isoformat(),
            'end': end_time.isoformat(),
            'color': colors[0],  #utiliser la première couleur de la liste des couleurs
            'extendedProps': {
                'duration': duration,
                'nbr_session': nbr_session,
                'capacity': room_capacity,
                'teacher': teacher_names,
                'room': room_names,
                'category': label_names,
                # 'roomdisponibilities': room_disponibilities,
                # 'teacherdisponibilities': teacher_disponibilities,
                # 'horrairedisponibilities': time_slots,
            },
        }

        events.append(event)
    return JsonResponse(events, safe=False)
