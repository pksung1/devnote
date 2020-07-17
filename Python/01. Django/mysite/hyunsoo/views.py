import os
from django.http import JsonResponse
from datetime import datetime

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from hyunsoo.models import HyunsooTodoList, HyunsooTodo


def first_api(request):
    return JsonResponse({'status': 200})


@csrf_exempt
def hyunsoo_todo(request, _id=None):
    result = {}
    if request.method == 'GET':
        # TODO: 원하는 조건으로 검색해서 리턴
        hyunsoo_todo_list = HyunsooTodoList()
        result['rows'] = hyunsoo_todo_list.json
    elif request.method == "POST":
        title = request.POST['title']
        context = request.POST.get('context', None)

        assert title and title.strip(), 'title 이 비어있습니다.'
        assert context and context.strip(), 'context 이 비어있습니다.'

        _hyunsoo_todo = HyunsooTodo(title=title, context=context)
        _hyunsoo_todo.write_db_file()

        assert _hyunsoo_todo.title == title
        assert _hyunsoo_todo.context == context

        hyunsoo_todo_list = HyunsooTodoList()
        result['rows'] = hyunsoo_todo_list.json
    elif request.method == "PUT":
        assert _id
        hyunsoo_todo_list = HyunsooTodoList()
        instance = hyunsoo_todo_list.get(_id=_id)
        instance.title = '수정된 값'
        instance.save()
    else:
        assert False
    return JsonResponse(result)
