from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.shortcuts import render, render_to_response
from django.http import JsonResponse, HttpResponse
from .models import *
from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder
from libgravatar import Gravatar
from django.db.models import Avg, Max, Min


def postdis(request):
    if request.method != 'POST':
        response_json_data = {
            'code': 404,
            'msg': '请使用POST请求'
        }
        return JsonResponse(response_json_data)

    received_json_data = json.loads(request.body)
    response_json_data = {
        'code': 200,
        'msg': '发布成功',
    }
    try:
        discuss = Discuss(
            student=Student.objects.get(
                student_id=received_json_data['userid']),
            text=received_json_data['text'],
        )
        discuss.save()
        return JsonResponse(response_json_data)
    except ObjectDoesNotExist:
        response_json_data["code"] = 404
        response_json_data["msg"] = "用户不存在"
        return JsonResponse(response_json_data)
    except ValueError:
        response_json_data["code"] = 404
        response_json_data["msg"] = "数据不正确"
        return JsonResponse(response_json_data)


def getDiscuss(request):
    discuss = Discuss.objects.all().order_by('-time')
    response_json_data = {
        'code': 200,
        'msg': '请求成功',
        'num': discuss.count(),
        'result': [],
    }
    for i in discuss:
        try:
            user = Admin.objects.get(id=i.student.student_id)
            if user.email is not None:
                image = Gravatar(user.email)
            else:
                image = "",
            response_json_data['result'].append({
                'discuss_id': i.discuss_id,
                'username': i.student.name,
                'img': image.get_image(),
                'class': i.student.classroom.name,
                'like_num': i.like_num,
                'text': i.text,
                'time': i.time.strftime("%Y-%m-%d %H:%I:%S"),
            })
        except ObjectDoesNotExist:
            response_json_data['result'].append({
                'discuss_id': i.discuss_id,
                'username': i.student.name,
                'img': '',
                'class': i.student.classroom.name,
                'like_num': i.like_num,
                'text': i.text,
                'time': i.time,
            })
    return JsonResponse(response_json_data)


def getComment(request, pk):
    response_json_data = {
        'code': 200,
        'msg': '发布成功',
        'num': 0,
        'result': []
    }
    try:
        comment = Comment.objects.filter(discuss__discuss_id=pk)
        response_json_data["num"] = comment.count()
        for i in comment:
            response_json_data['result'].append({
                'text': i.text,
                'username': i.student.name,
            })
        return JsonResponse(response_json_data)

    except ObjectDoesNotExist:
        response_json_data["code"] = 404
        response_json_data["msg"] = "帖子不存在"
        return JsonResponse(response_json_data)


def postcomment(request):
    if request.method != 'POST':
        response_json_data = {
            'code': 404,
            'msg': '请使用POST请求'
        }
        return JsonResponse(response_json_data)

    received_json_data = json.loads(request.body)
    response_json_data = {
        'code': 200,
        'msg': '评论成功',
    }
    try:
        comment = Comment(
            student=Student.objects.get(
                student_id=received_json_data['userid']),
            discuss=Discuss.objects.get(
                discuss_id=received_json_data['discuss_id']),
            text=received_json_data['text'],
        )
        comment.save()
        return JsonResponse(response_json_data)
    except ObjectDoesNotExist:
        response_json_data["code"] = 404
        response_json_data["msg"] = "用户不存在"
        return JsonResponse(response_json_data)


def addlike(request):
    if request.method != 'POST':
        response_json_data = {
            'code': 404,
            'msg': '请使用POST请求'
        }
        return JsonResponse(response_json_data)

    received_json_data = json.loads(request.body)
    response_json_data = {
        'code': 200,
        'msg': '点赞成功',
    }
    try:
        discuss = Discuss.objects.get(
            discuss_id=received_json_data['discuss_id'])
        discuss.like_num = discuss.like_num + 1
        discuss.save()
        return JsonResponse(response_json_data)
    except ObjectDoesNotExist:
        response_json_data["code"] = 404
        response_json_data["msg"] = "用户不存在"
        return JsonResponse(response_json_data)


def deletedis(request, pk):
    try:
        Discuss.objects.get(discuss_id=pk).delete()
        response_json_data = {
            'code': 200,
            'msg': '删除帖子成功',
        }
        return JsonResponse(response_json_data)
    except ObjectDoesNotExist:
        response_json_data = {
            'code': 404,
            'msg': '课程不存在',
        }
        return JsonResponse(response_json_data)
    # Create your views here.
