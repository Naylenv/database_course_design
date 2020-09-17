from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, render_to_response
from django.http import JsonResponse, HttpResponse
from .models import *
from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder
from libgravatar import Gravatar
from django.db.models import Avg, Max, Min


def toJSON(self):
    fields = []
    for field in self._meta.fields:
        fields.append(field.name)

    d = {}
    for attr in fields:
        d[attr] = getattr(self, attr)
    return json.dumps(d)


def hello(request):
    return JsonResponse({'result': 200, 'msg': '连接成功'})


def activitynum(request):
    num = Activity.objects.count()
    return JsonResponse({
        'code': 200,
        'msg': "获取成功",
        'num': num,
    })


def competitionnum(request):
    num = Competition.objects.count()
    return JsonResponse({
        'code': 200,
        'msg': "获取成功",
        'num': num,
    })


def examnum(request):
    num = Exam.objects.count()
    return JsonResponse({
        'code': 200,
        'msg': "获取成功",
        'num': num,
    })


def gpa(request, pk):
    elective = Elective.objects.filter(student__student_id=pk)
    sumscore = 0
    num = 0
    for i in elective:
        if i.score is not None:
            num = num + 1
            if i.score >= 60: sumscore = sumscore + (i.score / 10) - 5

    response_json_data = {
        'code': 200,
        'msg': '请求成功',
        'gpa': (sumscore / num),
    }

    return JsonResponse(response_json_data)


def todaycourse(request, pk):
    import math
    elective = Elective.objects.filter(student__student_id=pk)
    num = math.ceil((elective.count() / 5))
    if num > 5:
        num = 4
    response_json_data = {
        'code': 200,
        'msg': '请求成功',
        'num': num,
    }

    return JsonResponse(response_json_data)


def getStudent(request, pk):
    student = Student.objects.get(student_id=pk)
    # values('student_id', 'name', 'sex', 'phone_num', 'department', 'age', 'person_id', 'classroom')
    response_json_data = {
        'code': 200,
        'msg': '请求成功',
        'id': student.student_id,
        'sex': student.sex,
        'phone_num': student.phone_num,
        'age': student.age,
        'department_id': student.department.department_id,
        'department_name': student.department.name,
        'person_id': student.person_id,
        'classroom_id': student.classroom.classroom_id,
        'classroom_name': student.classroom.name,
        'name': student.name,
    }
    return JsonResponse(response_json_data)


def getTeacher(request, pk):
    teacher = Teacher.objects.get(teacher_id=pk)
    # values('student_id', 'name', 'sex', 'phone_num', 'department', 'age', 'person_id', 'classroom')
    response_json_data = {
        'code': 200,
        'msg': "获取成功",
        'id': teacher.teacher_id,
        'name': teacher.name,
        'sex': teacher.sex,
        'age': teacher.age,
        'phone_num': teacher.phone_num,
        'address': teacher.address,
        'department_name': teacher.department.name,
        'department_id': teacher.department.department_id,
        'person_id': teacher.person_id,
    }
    return JsonResponse(response_json_data)


def getAward(request, pk):
    award = Award.objects.filter(student__student_id=pk)
    response_json_data = {
        'code': 200,
        'msg': '请求成功',
        'num': award.count(),
        'result': [],
    }
    for i in award:
        response_json_data['result'].append({
            'type': i.style,
            'content': i.content,
            'time': i.time.strftime("%Y-%m-%d %H:%I:%S"),
            'flag': i.flag,

        })
    return JsonResponse(response_json_data)


def getDepart(request, pk):
    data = Department.objects.filter(cid=pk).values(
        "name", "address")
    data = json.dumps(list(data), cls=DjangoJSONEncoder)
    return HttpResponse(data, content_type='application/json')


def getExam(request, pk):  # get物体有属性值，是filer值
    exam = Exam.objects.get(exam_id=pk)
    data = {
        'name': exam.course.name,
        'time': exam.time,
        'address': exam.address,
    }
    return JsonResponse(data)
    # return HttpResponse(str(exam))


def getCompetition(request):
    competition = Competition.objects.all()
    response_json_data = {
        'code': 200,
        'msg': '请求成功',
        'num': competition.count(),
        'result': [],
    }
    for i in competition:
        response_json_data['result'].append({
            "com_id": i.competition_id,
            "name": i.name,
            "time": i.time,
            "address": i.address,
            "organizer": i.organizer,
            'info': i.info,
        })
    return JsonResponse(response_json_data)


def getActivity(request):  # get物体有属性值，是filer值
    activity = Activity.objects.all()
    response_json_data = {
        'code': 200,
        'msg': '请求成功',
        'num': activity.count(),
        'result': [],
    }
    for i in activity:
        response_json_data['result'].append({
            "activity_id": i.activity_id,
            "name": i.name,
            "time": i.time,
            "address": i.address,
            "organizer": i.organizer,
            "info": i.info,
        })
    return JsonResponse(response_json_data)


def get_activity_list(request):
    activity = Activity.objects.all()
    response_json_data = {
        'code': 200,
        'msg': '请求成功',
        'num': activity.count(),
        'result': [],
    }
    for i in activity:
        response_json_data['result'].append({
            "activity_id": i.activity_id,
            "name": i.name,
            "time": i.time,
            "address": i.address,
            "host": i.organizer,
            'info': i.info,
        })
    return JsonResponse(response_json_data)


def student_course_list(request, pk):
    elective = Elective.objects.filter(student__student_id=pk)
    response_json_data = {
        'code': 200,
        'msg': '请求成功',
        'num': elective.count(),
        'result': [],
    }
    for i in elective:
        response_json_data['result'].append({
            'course_id': i.course.course_id,
            'student_name': i.student.name,
            'classname': i.course.name,
            'time': i.course.time,
            'address': i.course.address,
            'teacher': i.course.teacher.name

        })
    return JsonResponse(response_json_data)

def gettestlist(request, pk):
    elective = Elective.objects.filter(student__student_id=pk)
    response_json_data = {
        'code': 200,
        'msg': '请求成功',
        'num': 0,
        'result': [],
    }
    for i in elective:
        try:
            exam = Exam.objects.get(course__course_id=i.course.course_id)
            response_json_data["num"] = response_json_data["num"] + 1
            response_json_data['result'].append({
                'course_id': i.course.course_id,
                'classname': i.course.name,
                'time': exam.time,
                'address': exam.address,
                'teacher': i.course.teacher.name
            })
            
        except ObjectDoesNotExist:
            continue
    return JsonResponse(response_json_data)


def teacher_course_list(request, pk):
    course = Course.objects.filter(teacher__teacher_id=pk)
    response_json_data = {
        'code': 200,
        'msg': '请求成功',
        'num': course.count(),
        'result': [],
    }
    for i in course:
        elective = Elective.objects.filter(
            course__course_id=i.course_id).distinct()
        response_json_data['result'].append({
            'course_id': i.course_id,
            'classname': i.name,
            'student_name': elective.count(),
            'time': i.time,
            'address': i.address,
            # 'teacher': i.teacher.name

        })
    return JsonResponse(response_json_data)


def deletecourse(request):
    if request.method != 'POST':
        response_json_data = {
            'code': 404,
            'msg': '请使用POST请求'
        }
        return JsonResponse(response_json_data)
    received_json_data = json.loads(request.body)

    if received_json_data.get('id') is None:
        response_json_data = {
            'code': 404,
            'msg': '请给我学生ID'
        }
        return JsonResponse(response_json_data)
    if received_json_data.get('course_id') is None:
        response_json_data = {
            'code': 404,
            'msg': '请给我课程ID'
        }
        return JsonResponse(response_json_data)
    elective = Elective.objects.filter(
        student__student_id=received_json_data['id'], course__course_id=received_json_data['course_id']).delete()
    response_json_data = {
        'code': 200,
        'msg': '退课成功',
    }
    return JsonResponse(response_json_data)


def choosenewcourse(request):
    if request.method != 'POST':
        response_json_data = {
            'code': 404,
            'msg': '请使用POST请求'
        }
        return JsonResponse(response_json_data)
    received_json_data = json.loads(request.body)

    if received_json_data.get('id') is None:
        response_json_data = {
            'code': 404,
            'msg': '请给我学生ID'
        }
        return JsonResponse(response_json_data)
    if received_json_data.get('course_id') is None:
        response_json_data = {
            'code': 404,
            'msg': '请给我课程ID'
        }
        return JsonResponse(response_json_data)
    try:
        data = Elective(
            student=Student.objects.get(student_id=received_json_data['id']),
            course=Course.objects.get(
                course_id=received_json_data['course_id'])
        )
        data.save()
        response_json_data = {
            'code': 200,
            'msg': '选课成功',
        }
        return JsonResponse(response_json_data)
    except ObjectDoesNotExist:
        response_json_data = {
            'code': 404,
            'msg': '学生不存在或课程不存在',
        }
        return JsonResponse(response_json_data)


def retakecourse(request):
    if request.method != 'POST':
        response_json_data = {
            'code': 404,
            'msg': '请使用POST请求'
        }
        return JsonResponse(response_json_data)
    received_json_data = json.loads(request.body)

    if received_json_data.get('id') is None:
        response_json_data = {
            'code': 404,
            'msg': '请给我学生ID'
        }
        return JsonResponse(response_json_data)
    if received_json_data.get('course_id') is None:
        response_json_data = {
            'code': 404,
            'msg': '请给我课程ID'
        }
        return JsonResponse(response_json_data)
    try:
        elective = Elective.objects.get(student__student_id=received_json_data['id'],
                                        course__course_id=received_json_data['course_id'])
        elective.retake = elective.retake + 1
        elective.save()
        response_json_data = {
            'code': 200,
            'msg': '重修成功',
        }
        return JsonResponse(response_json_data)
    except ObjectDoesNotExist:
        response_json_data = {
            'code': 404,
            'msg': '学生不存在或课程不存在',
        }
        return JsonResponse(response_json_data)


def getselectedcourse(request):
    if request.method != 'POST':
        response_json_data = {
            'code': 404,
            'msg': '请使用POST请求'
        }
        return JsonResponse(response_json_data)

    received_json_data = json.loads(request.body)
    course = Course.objects.filter()
    if received_json_data.get("course_id"):
        course = course.filter(course_id__contains=received_json_data["course_id"])
    if received_json_data.get('name'):
        course = course.filter(name__contains=received_json_data['name'])
    if received_json_data.get('time'):
        course = course.filter(time__contains=received_json_data['time'])
    if received_json_data.get('teacher'):
        course = course.filter(teacher__name__contains=received_json_data['teacher'])
    if received_json_data.get('department'):
        course = course.filter(
            department__name__contains=received_json_data['department'])

    response_json_data = {
        'code': 200,
        'msg': '请求成功',
        'num': course.count(),
        'result': [],
    }
    for i in course:
        response_json_data['result'].append({
            'course_id': i.course_id,
            'classname': i.name,
            'time': i.time,
            'address': i.address,
            'teacher': i.teacher.name,
            'department': i.department.name,

        })
    return JsonResponse(response_json_data)


# def get_token(request):
#     token = get_token(request)
#     return JsonResponse({'token': token})


def postcom(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        data = Competition(
            name=received_json_data['name'],
            time=received_json_data['time'],
        )
        if received_json_data.get('address'):
            data.address = received_json_data["address"]
        if received_json_data.get('info'):
            data.info = received_json_data["info"]
        if received_json_data.get('organizer'):
            data.organizer = received_json_data["organizer"]
        data.save()
        response_json_data = {
            'code': 200,
            "msg": '发布成功',
        }
        return JsonResponse(response_json_data)
    else:
        response_json_data = {
            'code': 404,
            "msg": '请使用POST',
        }
        return JsonResponse(response_json_data)


def postact(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        data = Activity(
            name=received_json_data['name'],
            time=received_json_data['time'],
        )
        if received_json_data.get('address'):
            data.address = received_json_data["address"]
        if received_json_data.get('info'):
            data.info = received_json_data["info"]
        if received_json_data.get('Organizer'):
            data.style = received_json_data["Organizer"]
        data.save()
        response_json_data = {
            'code': 200,
            "msg": '发布成功',
        }
        return JsonResponse(response_json_data)
    else:
        response_json_data = {
            'code': 404,
            "msg": '请使用POST',
        }
        return JsonResponse(response_json_data)


def postexam(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        data = Exam(
            name=received_json_data['name'],
            time=received_json_data['time'],
        )
        if received_json_data.get('address'):
            data.address = received_json_data["address"]
        data.save()
        response_json_data = {
            'code': 200,
            "msg": '发布成功',
        }
        return JsonResponse(response_json_data)
    else:
        response_json_data = {
            'code': 404,
            "msg": '请使用POST',
        }
        return JsonResponse(response_json_data)


def login(request):
    if (request.method == 'POST'):
        received_json_data = json.loads(request.body)
        response_json_data = {}
        try:
            user = Admin.objects.get(id=received_json_data["id"])
        except ObjectDoesNotExist:
            response_json_data["code"] = 404
            response_json_data["msg"] = "用户不存在"
            return JsonResponse(response_json_data)
        try:
            Student.objects.get(student_id=user.id)
            response_json_data["user"] = "student"
        
        except ObjectDoesNotExist:
            try:
                Teacher.objects.get(teacher_id=user.id)
                response_json_data["user"] = "teacher"
            except ObjectDoesNotExist:
                response_json_data["user"] = "admin"
            

        if user.pwd == received_json_data["pwd"]:
            response_json_data["code"] = 200
            response_json_data["msg"] = "登入成功"
            return JsonResponse(response_json_data)
        else:
            response_json_data["code"] = 404
            response_json_data["msg"] = "密码错误"
            return JsonResponse(response_json_data)


def userinfo(request, pk):
    response_json_data = {}
    try:
        user = Admin.objects.get(id=pk)
        response_json_data['nickname'] = user.nickname
        response_json_data['email'] = user.email
        response_json_data['type'] = user.usertype
        response_json_data['image'] = ""
        if user.email is not None:
            image = Gravatar(user.email)
            response_json_data['image'] = image.get_image()
        if user.usertype == 2:
            info = Student.objects.get(student_id=pk)
            response_json_data['name'] = info.name
            response_json_data['id'] = info.student_id
            response_json_data['classroom'] = info.classroom.name
            response_json_data['classroom_id'] = info.classroom_id
            response_json_data['department_name'] = info.department.name
            response_json_data['department_id'] = info.department.department_id
            response_json_data['sex'] = info.sex
            response_json_data['age'] = info.age
            response_json_data['person_id'] = info.person_id
            response_json_data['phone_num'] = info.phone_num
        elif user.usertype == 1:
            info = Teacher.objects.get(teacher_id=pk)
            response_json_data['id'] = info.teacher_id
            response_json_data['department_id'] = info.department_id
            response_json_data['age'] = info.age
            response_json_data['name'] = info.name
            response_json_data['department_name'] = info.department.name
            response_json_data['department_id'] = info.department.department_id
            response_json_data['address'] = info.address
            response_json_data['sex'] = info.sex
            response_json_data['person_id'] = info.person_id
            response_json_data['phone_num'] = info.phone_num
        response_json_data["code"] = 200
        response_json_data["msg"] = "获取成功"
        return JsonResponse(response_json_data)

    except ObjectDoesNotExist:
        response_json_data["code"] = 404
        response_json_data["msg"] = "用户不存在"
        return JsonResponse(response_json_data)


def joinact(request):
    if request.method != 'POST':
        response_json_data = {
            'code': 404,
            'msg': '请使用POST请求'
        }
        return JsonResponse(response_json_data)
    received_json_data = json.loads(request.body)

    if received_json_data.get('user_id') is None:
        response_json_data = {
            'code': 404,
            'msg': '请给我学生ID'
        }
        return JsonResponse(response_json_data)
    if received_json_data.get('activity_id') is None:
        response_json_data = {
            'code': 404,
            'msg': '请给我活动ID'
        }
        return JsonResponse(response_json_data)
    try:
        exitstudent = Act_Stu.objects.filter(
            student__student_id=received_json_data['user_id'],
            activity__activity_id=received_json_data['activity_id']
        )
        if exitstudent.exists() == 1:
            response_json_data = {
                'code': 404,
                'msg': '您已报名',
            }
            return JsonResponse(response_json_data)
        data = Act_Stu(
            student=Student.objects.get(
                student_id=received_json_data['user_id']),
            activity=Activity.objects.get(
                activity_id=received_json_data['activity_id'])
        )
        data.save()
        response_json_data = {
            'code': 200,
            'msg': '报名成功',
        }
        return JsonResponse(response_json_data)
    except ObjectDoesNotExist:
        response_json_data = {
            'code': 404,
            'msg': '学生不存在或活动不存在',
        }
        return JsonResponse(response_json_data)


def joincom(request):
    if request.method != 'POST':
        response_json_data = {
            'code': 404,
            'msg': '请使用POST请求'
        }
        return JsonResponse(response_json_data)
    received_json_data = json.loads(request.body)

    if received_json_data.get('user_id') is None:
        response_json_data = {
            'code': 404,
            'msg': '请给我学生ID'
        }
        return JsonResponse(response_json_data)
    if received_json_data.get('com_id') is None:
        response_json_data = {
            'code': 404,
            'msg': '请给我比赛ID'
        }
        return JsonResponse(response_json_data)
    try:
        exitstudent = Com_Stu.objects.filter(
            student__student_id=received_json_data['user_id'],
            competition__competition_id=received_json_data['com_id']
        )
        if exitstudent.exists() == 1:
            response_json_data = {
                'code': 404,
                'msg': '您已报名',
            }
            return JsonResponse(response_json_data)

        data = Com_Stu(
            student=Student.objects.get(
                student_id=received_json_data['user_id']),
            competition=Competition.objects.get(
                competition_id=received_json_data['com_id'])
        )
        data.save()
        response_json_data = {
            'code': 200,
            'msg': '报名成功',
        }
        return JsonResponse(response_json_data)
    except ObjectDoesNotExist:
        response_json_data = {
            'code': 404,
            'msg': '学生不存在或比赛不存在',
        }
        return JsonResponse(response_json_data)


def getstudentlist(request):
    if request.method != 'POST':
        response_json_data = {
            'code': 404,
            'msg': '请使用POST请求'
        }
        return JsonResponse(response_json_data)

    received_json_data = json.loads(request.body)
    if received_json_data.get('course_id') is None:
        response_json_data = {
            'code': 404,
            'msg': '请给我课程ID'
        }
        return JsonResponse(response_json_data)

    elective = Elective.objects.filter(
        course__course_id=received_json_data["course_id"])
    response_json_data = {
        'code': 200,
        'msg': '请求成功',
        'num': elective.count(),
        'result': [],
    }
    for i in elective:
        response_json_data['result'].append({
            'id': i.student.student_id,
            'name': i.student.name,
            'classroom': i.student.classroom.name,
            'department': i.student.department.name,
            # 'time': i.course.time,
            # 'address': i.course.address,
            'retake': i.retake,
            'score': i.score,
            # 'teacher': i.course.teacher.name

        })
    return JsonResponse(response_json_data)


def startnewcourse(request):
    if request.method != 'POST':
        response_json_data = {
            'code': 404,
            'msg': '请使用POST请求'
        }
        return JsonResponse(response_json_data)
    received_json_data = json.loads(request.body)

    if received_json_data.get('teacher_id') is None:
        response_json_data = {
            'code': 404,
            'msg': '请给我教师ID'
        }
        return JsonResponse(response_json_data)
    if received_json_data.get('classname') is None:
        response_json_data = {
            'code': 404,
            'msg': '请给我课程名'
        }
        return JsonResponse(response_json_data)
    if received_json_data.get('department_id') is None:
        response_json_data = {
            'code': 404,
            'msg': '请给我开课学院ID'
        }
        return JsonResponse(response_json_data)
    if received_json_data.get('course_id') is None:
        response_json_data = {
            'code': 404,
            'msg': '请给我课程ID'
        }
        return JsonResponse(response_json_data)
    try:
        data = Course(
            teacher=Teacher.objects.get(
                teacher_id=received_json_data["teacher_id"]),
            department=Department.objects.get(
                department_id=received_json_data["department_id"])
        )
        data.course_id = received_json_data["course_id"]
        data.name = received_json_data["classname"]
        if received_json_data.get('time'):
            data.time = received_json_data["time"]
        if received_json_data.get('address'):
            data.address = received_json_data["address"]
        data.save()
        response_json_data = {
            'code': 200,
            'msg': '开课成功',
        }
        return JsonResponse(response_json_data)
    except ObjectDoesNotExist:
        response_json_data = {
            'code': 404,
            'msg': '教师或学院不存在',
        }
        return JsonResponse(response_json_data)


def getcoursegrade(request, pk):
    elective = Elective.objects.filter(student__student_id=pk)
    response_json_data = {
        'code': 200,
        'msg': '请求成功',
        'num': elective.count(),
        'result': [],
    }
    for i in elective:
        the_course = Elective.objects.filter(
            course__course_id=i.course.course_id)
        # the_course.order_by('-score').distinct()
        sumnum = the_course.count()
        if i.score is not None:
            over_student = the_course.filter(score__gte=i.score)
            response_json_data['result'].append({
                'course_id': i.course.course_id,
                # 'student_name': i.student.name,
                'retake':i.retake,
                'classname': i.course.name,
                'teacher': i.course.teacher.name,
                'score': i.score,
                'rank': str(over_student.count())+'/' + str(sumnum),

            })
        else:
            response_json_data['result'].append({
                'course_id': i.course.course_id,
                # 'student_name': i.student.name,
                'classname': i.course.name,
                'teacher': i.course.teacher.name,
                # 'score': i.score,
                # 'rank': str(over_student.count())+'/' + str(sumnum),
            })

    return JsonResponse(response_json_data)


def changerpinfo(request):
    if request.method != 'POST':
        response_json_data = {
            'code': 404,
            'msg': '请使用POST请求'
        }
        return JsonResponse(response_json_data)
    received_json_data = json.loads(request.body)

    if received_json_data.get('id') is None:
        response_json_data = {
            'code': 404,
            'msg': '请给我学生ID'
        }
        return JsonResponse(response_json_data)
    try:
        award = Award(
            student = Student.objects.get(student_id=received_json_data["id"]),
            flag = received_json_data["flag"],
            style = received_json_data["type"],
            content = received_json_data["content"],

        )
        award.save()
        response_json_data = {
            'code': 200,
            'msg': '奖惩录入成功',
        }
        return JsonResponse(response_json_data)
    except ObjectDoesNotExist:
        response_json_data = {
            'code': 404,
            'msg': '学生不存在',
        }
        return JsonResponse(response_json_data)

def enrollgrade(request):
    if request.method != 'POST':
        response_json_data = {
            'code': 404,
            'msg': '请使用POST请求'
        }
        return JsonResponse(response_json_data)
    received_json_data = json.loads(request.body)

    if received_json_data.get('id') is None:
        response_json_data = {
            'code': 404,
            'msg': '请给我学生ID'
        }
        return JsonResponse(response_json_data)
    if received_json_data.get('course_id') is None:
        response_json_data = {
            'code': 404,
            'msg': '请给我课程ID'
        }
        return JsonResponse(response_json_data)
    if received_json_data.get('score') is None or type(received_json_data['score']) != int:
        response_json_data = {
            'code': 404,
            'msg': '请给我成绩或成绩无效'
        }
        return JsonResponse(response_json_data)
    try:
        elective = Elective.objects.get(student__student_id=received_json_data['id'],
                                        course__course_id=received_json_data['course_id'])
        elective.score = received_json_data['score']
        elective.save()
        response_json_data = {
            'code': 200,
            'msg': '成绩录入成功',
        }
        return JsonResponse(response_json_data)
    except ObjectDoesNotExist:
        response_json_data = {
            'code': 404,
            'msg': '学生不存在或课程不存在或成绩不正确',
        }
        return JsonResponse(response_json_data)


def getgradeanalyse(request):
    if request.method != 'POST':
        response_json_data = {
            'code': 404,
            'msg': '请使用POST请求'
        }
        return JsonResponse(response_json_data)
    received_json_data = json.loads(request.body)

    if received_json_data.get('course_id') is None:
        response_json_data = {
            'code': 404,
            'msg': '请给我课程ID'
        }
        return JsonResponse(response_json_data)
    elective = Elective.objects.filter(
        course__course_id=received_json_data["course_id"])
    if elective.count() <= 0:
        response_json_data = {
            'code': 404,
            'msg': '该课没有人选呢，亲!',
        }
        return JsonResponse(response_json_data)
    response_json_data = {
        'code': 200,
        'msg': '请求成功',
    }
    agg_score = elective.aggregate(Avg('score'), Max('score'), Min('score'))
    response_json_data["max"] = agg_score["score__max"]
    response_json_data["min"] = agg_score["score__min"]
    response_json_data["avg"] = agg_score["score__avg"]
    pass_student = elective.filter(score__gte=60)
    response_json_data["passrate"] = 100 * \
        (pass_student.count() / elective.count())
    # for i in elective:
    #     # the_course = Elective.objects.filter(course__course_id=i.course.course_id)
    #     # the_course.order_by('-score').distinct()
    #     # sumnum = the_course.count()
    #     # rank = 1
    #     # for j in the_course:
    #     #     if j.student.student_id != i.student.student_id:
    #     #         rank = rank + 1
    #     #     else:
    #     #         break
    #     response_json_data['result'].append({
    #         'course_id': i.course.course_id,
    #         #'student_name': i.student.name,
    #         'classname':i.course.name,
    #         'teacher': i.course.teacher.name,
    #         'score': i.score,
    #         # 'rank':str(rank)+'/' + str(sumnum),

    #     })
    return JsonResponse(response_json_data)


def studentinfo(request):
    student = Student.objects.all()
    response_json_data = {
        'code': 200,
        'msg': '请求成功',
        'num': student.count(),
        'result': [],
    }
    for i in student:
        response_json_data['result'].append({
            'id': i.student_id,
            'name': i.name,
            'sex': i.sex,
            'phone_num': i.phone_num,
            'department': i.department.name,
            'person_id': i.person_id,
            'age': i.age,
            'classroom': i.classroom.name,
            # 'time': i.course.time,
            # 'address': i.course.address,
            # 'retake': i.retake,
            # 'score': i.score,
            # 'teacher': i.course.teacher.name

        })
    return JsonResponse(response_json_data)


def teacherinfo(request):
    teacher = Teacher.objects.all()
    response_json_data = {
        'code': 200,
        'msg': '请求成功',
        'num': teacher.count(),
        'result': [],
    }
    for i in teacher:
        response_json_data['result'].append({
            'id': i.teacher_id,
            'name': i.name,
            'sex': i.sex,
            'phone_num': i.phone_num,
            'department': i.department.name,
            'person_id': i.person_id,
            'age': i.age,
        })
    return JsonResponse(response_json_data)


def getselectedstudent(request):
    if request.method != 'POST':
        response_json_data = {
            'code': 404,
            'msg': '请使用POST请求'
        }
        return JsonResponse(response_json_data)

    received_json_data = json.loads(request.body)
    student = Student.objects.all()
    if received_json_data.get("id"):
        student = student.filter(student_id__contains=received_json_data["id"])
    if received_json_data.get('name'):
        student = student.filter(name__contains=received_json_data['name'])
    if received_json_data.get('department'):
        student = student.filter(
            department__name__contains=received_json_data['department'])
    if received_json_data.get('classroom'):
        student = student.filter(
            classroom__name__contains=received_json_data['classroom'])

    response_json_data = {
        'code': 200,
        'msg': '请求成功',
        'num': student.count(),
        'result': [],
    }
    for i in student:
        response_json_data['result'].append({
            'id': i.student_id,
            'name': i.name,
            'department': i.department.name,
            'classroom': i.classroom.name,

        })
    return JsonResponse(response_json_data)

def getselectedteacher(request):
    if request.method != 'POST':
        response_json_data = {
            'code': 404,
            'msg': '请使用POST请求'
        }
        return JsonResponse(response_json_data)

    received_json_data = json.loads(request.body)
    teacher = Teacher.objects.all()
    if received_json_data.get("id"):
        teacher = teacher.filter(teacher_id__contains=received_json_data["id"])
    if received_json_data.get('name'):
        teacher = teacher.filter(name__contains=received_json_data['name'])
    if received_json_data.get('department'):
        teacher = teacher.filter(
            department__name__contains=received_json_data['department'])
    if received_json_data.get('address'):
        teacher = teacher.filter(
            teacher__contains=received_json_data['address'])

    response_json_data = {
        'code': 200,
        'msg': '请求成功',
        'num': teacher.count(),
        'result': [],
    }
    for i in teacher:
        response_json_data['result'].append({
            'id': i.teacher_id,
            'name': i.name,
            'department': i.department.name,
            'address': i.address,

        })
    return JsonResponse(response_json_data)

def getalldepartment(request):
    department = Department.objects.all()
    response_json_data = {
        'code': 200,
        'msg': '请求成功',
        'num': department.count(),
        'result': [],
    }
    for i in department:
        response_json_data['result'].append({
            'department_id': i.department_id,
            'department_name': i.name,
        })
    return JsonResponse(response_json_data)

def getallclass(request,pk):
    classroom = Classroom.objects.filter(department__department_id = pk)
    response_json_data = {
        'code': 200,
        'msg': '请求成功',
        'num': classroom.count(),
        'result': [],
    }
    for i in classroom:
        response_json_data['result'].append({
            'class_id': i.classroom_id,
            'class_name': i.name,
        })
    return JsonResponse(response_json_data)

def changestudentinfo(request):
    if request.method != 'POST':
        response_json_data = {
            'code': 404,
            'msg': '请使用POST请求'
        }
        return JsonResponse(response_json_data)
    received_json_data = json.loads(request.body)
    try: 
        student = Student.objects.get(student_id=received_json_data["id"])
        student.department = Department.objects.get(department_id=received_json_data["department_id"])
        student.classroom = Classroom.objects.get(classroom_id=received_json_data["classroom_id"])
        student.name = received_json_data["name"]
        student.sex = received_json_data["sex"]
        student.age = received_json_data["age"]
        student.person_id = received_json_data["person_id"]
        student.phone_num = received_json_data["phone_num"]
        student.save()
        response_json_data = {
            'code': 200,
            'msg': '修改成功',
        }
        return JsonResponse(response_json_data)
    except ObjectDoesNotExist:
        response_json_data = {
            'code': 404,
            'msg': '学生或学院或班级不存在。惊了',
        }
        return JsonResponse(response_json_data)

def changeteacherinfo(request):
    if request.method != 'POST':
        response_json_data = {
            'code': 404,
            'msg': '请使用POST请求'
        }
        return JsonResponse(response_json_data)
    received_json_data = json.loads(request.body)
    try: 
        teacher = Teacher.objects.get(teacher_id=received_json_data["id"])
        teacher.department = Department.objects.get(department_id=received_json_data["department_id"])
        teacher.name = received_json_data["name"]
        teacher.sex = received_json_data["sex"]
        teacher.age = received_json_data["age"]
        teacher.address = received_json_data["address"]
        teacher.person_id = received_json_data["person_id"]
        teacher.phone_num = received_json_data["phone_num"]
        teacher.save()
        response_json_data = {
            'code': 200,
            'msg': '修改成功',
        }
        return JsonResponse(response_json_data)
    except ObjectDoesNotExist:
        response_json_data = {
            'code': 404,
            'msg': '学生或学院或班级不存在。惊了',
        }
        return JsonResponse(response_json_data)

def changedepartmentinfo(request):
    if request.method != 'POST':
        response_json_data = {
            'code': 404,
            'msg': '请使用POST请求'
        }
        return JsonResponse(response_json_data)
    received_json_data = json.loads(request.body)
    try: 
        department = Department.objects.get(department_id=received_json_data["department_id"])
        department.name = received_json_data["department_name"]
        department.save()
        response_json_data = {
            'code': 200,
            'msg': '修改成功',
        }
        return JsonResponse(response_json_data)
    except ObjectDoesNotExist:
        response_json_data = {
            'code': 404,
            'msg': '学院不存在!!!',
        }
        return JsonResponse(response_json_data)

def changeclassinfo(request):
    if request.method != 'POST':
        response_json_data = {
            'code': 404,
            'msg': '请使用POST请求'
        }
        return JsonResponse(response_json_data)
    received_json_data = json.loads(request.body)
    try: 
        course = Course.objects.get(course_id=received_json_data["course_id"])
        course.time = received_json_data["time"]
        course.address = received_json_data["address"]
        course.save()
        response_json_data = {
            'code': 200,
            'msg': '修改成功',
        }
        return JsonResponse(response_json_data)
    except ObjectDoesNotExist:
        response_json_data = {
            'code': 404,
            'msg': '课程不存在!!!',
        }
        return JsonResponse(response_json_data)


def deletecom(request, pk):
    try:
        Competition.objects.get(competition_id=pk).delete()
        response_json_data = {
            'code': 200,
            'msg': '删除比赛成功',
        }
        return JsonResponse(response_json_data)
    except ObjectDoesNotExist:
        response_json_data = {
            'code': 404,
            'msg': '比赛不存在',
        }
        return JsonResponse(response_json_data)

def deleteteacher(request, pk):
    try:
        Teacher.objects.get(teacher_id=pk).delete()
        response_json_data = {
            'code': 200,
            'msg': '删除教师成功',
        }
        return JsonResponse(response_json_data)
    except ObjectDoesNotExist:
        response_json_data = {
            'code': 404,
            'msg': '教师不存在',
        }
        return JsonResponse(response_json_data)

def deletestudent(request, pk):
    try:
        Student.objects.get(student_id=pk).delete()
        response_json_data = {
            'code': 200,
            'msg': '删除学生成功',
        }
        return JsonResponse(response_json_data)
    except ObjectDoesNotExist:
        response_json_data = {
            'code': 404,
            'msg': '学生不存在',
        }
        return JsonResponse(response_json_data)

def deleteact(request, pk):
    try:
        Activity.objects.get(activity_id=pk).delete()
        response_json_data = {
            'code': 200,
            'msg': '删除活动成功',
        }
        return JsonResponse(response_json_data)
    except ObjectDoesNotExist:
        response_json_data = {
            'code': 404,
            'msg': '活动不存在',
        }
        return JsonResponse(response_json_data)


def enrollnewstudent(request):
    if request.method != 'POST':
        response_json_data = {
            'code': 404,
            'msg': '请使用POST请求'
        }
        return JsonResponse(response_json_data)

    received_json_data = json.loads(request.body)
    response_json_data = {
        'code': 200,
        'msg': '录入成功',
    }
    try:
        student = Student(
            student_id=received_json_data['id'],
            name=received_json_data['name'],
            department=Department.objects.get(
                department_id=received_json_data['department_id']),
            classroom=Classroom.objects.get(
                classroom_id=received_json_data['classroom_id'])
        )
        if received_json_data.get("age"):
            student.age = received_json_data["age"]
        if received_json_data.get("sex") :
            student.sex = received_json_data["sex"]
        if received_json_data.get("person_id") :
            student.person_id = received_json_data["person_id"]
        if received_json_data.get("phone_num") :
            student.phone_num= received_json_data["phone_num"]
        student.save()
        return JsonResponse(response_json_data)
    except ObjectDoesNotExist:
        response_json_data["code"] = 404
        response_json_data["msg"] = "学院或班级不存在"
        return JsonResponse(response_json_data)
    except ValueError:
        response_json_data["code"] = 404
        response_json_data["msg"] = "数据不正确"
        return JsonResponse(response_json_data)
        
def enrollnewteacher(request):
    if request.method != 'POST':
        response_json_data = {
            'code': 404,
            'msg': '请使用POST请求'
        }
        return JsonResponse(response_json_data)

    received_json_data = json.loads(request.body)
    response_json_data = {
        'code': 200,
        'msg': '录入成功',
    }
    try:
        teacher = Teacher(
            teacher_id=received_json_data['id'],
            name=received_json_data['name'],
            department=Department.objects.get(
                department_id=received_json_data['department_id'])
        )
        if received_json_data.get("age"):
            teacher.age = received_json_data["age"]
        if received_json_data.get("sex") :
            teacher.sex = received_json_data["sex"]
        if received_json_data.get("person_id") :
            teacher.person_id = received_json_data["person_id"]
        if received_json_data.get("phone_num") :
            teacher.phone_num = received_json_data["phone_num"]
        if received_json_data.get("address") :
            teacher.address= received_json_data["address"]
        teacher.save()
        return JsonResponse(response_json_data)
    except ObjectDoesNotExist:
        response_json_data["code"] = 404
        response_json_data["msg"] = "学院不存在"
        return JsonResponse(response_json_data)
    except ValueError:
        response_json_data["code"] = 404
        response_json_data["msg"] = "数据不正确"
        return JsonResponse(response_json_data)

def enrolltest(request):
    if request.method != 'POST':
        response_json_data = {
            'code': 404,
            'msg': '请使用POST请求'
        }
        return JsonResponse(response_json_data)

    received_json_data = json.loads(request.body)
    response_json_data = {
        'code': 200,
        'msg': '排课成功',
    }
    try:
        getExam = Exam.objects.filter(course__course_id=received_json_data['course_id']).exists()
        if getExam:
            getExam = Exam.objects.get(course__course_id=received_json_data['course_id'])
            getExam.time = received_json_data['time']
            getExam.address = received_json_data['address']
            getExam.save()
        else:
            exam = Exam(
                address=received_json_data['address'],
                time=received_json_data['time'],
                course=Course.objects.get(
                    course_id=received_json_data['course_id'])
            )
            exam.save()
        return JsonResponse(response_json_data)
    except ObjectDoesNotExist:
        response_json_data["code"] = 404
        response_json_data["msg"] = "课程不存在"
        return JsonResponse(response_json_data)
    except ValueError:
        response_json_data["code"] = 404
        response_json_data["msg"] = "数据不正确"
        return JsonResponse(response_json_data)

def enrollnewdepartment(request):
    if request.method != 'POST':
        response_json_data = {
            'code': 404,
            'msg': '请使用POST请求'
        }
        return JsonResponse(response_json_data)

    received_json_data = json.loads(request.body)
    response_json_data = {
        'code': 200,
        'msg': '新增学院成功',
    }
    try:
        department = Department(
           name=received_json_data["department_name"]
            
        )
        department.save()
        return JsonResponse(response_json_data)
    except ValueError:
        response_json_data["code"] = 404
        response_json_data["msg"] = "数据不正确"
        return JsonResponse(response_json_data)

def enrollnewclass(request):
    if request.method != 'POST':
        response_json_data = {
            'code': 404,
            'msg': '请使用POST请求'
        }
        return JsonResponse(response_json_data)

    received_json_data = json.loads(request.body)
    response_json_data = {
        'code': 200,
        'msg': '新增班级成功',
    }
    try:
        classroom = Classroom(
            department=Department.objects.get(department_id=received_json_data["department_id"]),
            name=received_json_data["class_name"]
        )
        classroom.save()
        return JsonResponse(response_json_data)
    except ValueError:
        response_json_data["code"] = 404
        response_json_data["msg"] = "数据不正确"
        return JsonResponse(response_json_data)
