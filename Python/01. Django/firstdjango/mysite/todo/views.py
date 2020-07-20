from django.http import HttpResponse, JsonResponse, QueryDict

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json
from .models import TodoListItem


@csrf_exempt
def index(request):
    ret = {'msg': 'no result'}
    if request.method == 'GET':
        ret = read_todo_list_items()
    elif request.method == 'POST':
        todo_text = request.POST.get('todo', None)
        ret = create_todo_item(todo_text)
    elif request.method == 'PUT':
        if request.content_type == 'application/json':
            request_json = json.loads(request.body.decode('ascii'))
            id = request_json.get('id', None)
            todo_text = request_json.get('todo', None)
            ret = update_todo_item(id, todo_text)
        else:
            ret = {'msg': 'PUT', 'data': []}
    elif request.method == 'DELETE':
        if request.content_type == 'application/json':
            request_json = json.loads(request.body.decode('ascii'))
            id = request_json.get('id', None)
            ret = delete_todo_item(id)
    return JsonResponse(ret)

def read_todo_list_items():
    return {'msg': 'GET', 'data': show_all_json_todolist()}

def create_todo_item(todo_text):
    todo_item = TodoListItem(todo=todo_text)
    todo_item.save()
    return {'msg': 'POST', 'data': show_all_json_todolist()}

def update_todo_item(id, todo_text):
    item = None
    try:
        item = TodoListItem.objects.get(id=id)
    except:
        print('Error Trying Find TodoListItem as id => [%d]' % id)
    item.todo = todo_text
    item.save()
    return {'msg': 'UPDATE', 'data': show_all_json_todolist()}

def delete_todo_item(id):
    try:
        item = TodoListItem.objects.get(id=id)
        item.delete()
    except:
        print('Delete Trying find TodoListItem [%d]' % id)
    return {'msg': 'DELETE', 'data': show_all_json_todolist()}

def show_all_json_todolist():
    return [item.json for item in TodoListItem.objects.all()]
