from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
import os

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from seonpark.models import TodoList


def seon_api(request):
    return JsonResponse({'status': 200, 'data': 'hello world'})

@csrf_exempt
def todo_list(request, reg_id=None, reg_title=None):
    seon_todo_list = TodoList().getItems()
    response = dict({})
    if request.method == 'GET':
        response = seon_todo_list.getItems().json()
    elif request.method == 'POST':
        title = request.POST.get('title', None)
        context = request.POST.get('context', None)
        response = seon_todo_list.getItems().create(title=title, context=context).save().getItems().json()
    elif request.method == 'PUT':
        print("regs!!", reg_id, reg_title)
        title = request.POST.get('title', None)
        context = request.POST.get('context', None)
        print(title, context)
        response = seon_todo_list.update(id=reg_id, title=reg_title).save().getItems().json()
    elif request.method == 'DELETE':
        delete_todos = seon_todo_list.filter(func_filter, title=reg_title)
        response = seon_todo_list.delete(delete_todos).save().getItems().json()

    return JsonResponse(dict({'row': response}))


def update_todo(request, id=None):
    pass


def func_filter(todos, title=None, context=None, id=None):
    return [todo for todo in todos if todo.id == id or todo.title == title or todo.context == context]

