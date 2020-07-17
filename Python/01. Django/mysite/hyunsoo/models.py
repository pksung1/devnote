import os
from datetime import datetime


class HyunsooTodoList(object):
    def __init__(self):
        self._hyunsoo_todos = []

    def filter(self, _id):
        return list(filter(lambda todo: todo._id == _id, self.hyunsoo_todos))

    def get(self, _id):
        return [item for item in self.hyunsoo_todos if item.id == _id][0]

    @property
    def hyunsoo_todos(self):
        if self._hyunsoo_todos:
            return self._hyunsoo_todos

        if not os.path.exists('hyunsoo/file_db/hyunsoo_todo.tsv'):
            with open('hyunsoo/file_db/hyunsoo_todo.tsv', 'w') as f:
                first_line = '{}\t{}\t{}\n'.format('id', 'title', 'context')
                f.write(first_line)
        all_data = []
        with open('hyunsoo/file_db/hyunsoo_todo.tsv', 'r') as f:
            for index, line in enumerate(f):
                if index == 0:
                    continue
                line = line.strip()
                splited_values = line.split('\t')
                _d = {
                    'index': index,
                    'id': splited_values[0],
                    'title': splited_values[1],
                    'context': splited_values[2],
                }
                all_data.append(_d)

        for item in all_data:
            self._hyunsoo_todos.append(
                HyunsooTodo(**item)
            )
        return self._hyunsoo_todos

    @hyunsoo_todos.setter
    def hyunsoo_todos(self, v):
        assert v
        self._hyunsoo_todos = v

    @property
    def json(self):
        _d = []
        for todo in self.hyunsoo_todos:
            _d.append({
                "id": todo._id,
                "title": todo.title,
                "context": todo.context
            })
        return _d


# Create your models here.
class HyunsooTodo(object):
    def __init__(self, index, id=None, title=None, context=None):
        self.index = index
        self._id = id or datetime.now().timestamp()
        self.title = title or 'title_{}'.format(self._id)
        self.context = context or 'context_{}'.format(self._id)

    @property
    def json(self):
        return {
            'id': self._id,
            'title': self.title,
            'context': self.context,
        }

    def save(self):
        pass

    def write_db_file(self):
        _id = self._id
        title = self.title
        context = self.context
        with open('hyunsoo/file_db/hyunsoo_todo.tsv', 'a') as f:
            f.write(
                '{}\t{}\t{}\n'.format(_id, title, context))
