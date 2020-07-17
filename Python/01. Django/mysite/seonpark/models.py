import os
from datetime import datetime

from decorator import __init__
from django.db import models

# Create your models here.

class TodoList(object):
    def __init__(self):
        self._todoList = list()
        self._filepath = 'seonpark/file_db/todolist.csv'
        self._keys = ['id', 'title', 'context']

        if not os.path.exists(self._filepath):
            with open(self._filepath, 'w') as f:
                f.write('\t'.join(self._keys) + '\n')

    @property
    def todoList(self):
        return self._todoList

    def getItems(self):
        result = list()
        with open(self._filepath, 'r') as f:
            for index, line in enumerate(f):
                if index == 0:
                    keys = line.strip().split('\t')
                    continue
                result.append(TodoListItem(**dict(zip(keys, line.strip().split('\t')))))
        self._todoList = result
        return self

    def create(self, title=None, context=None):
        item = TodoListItem(title=title, context=context)
        self._todoList.append(item)
        print("{} created {}".format('=' * 5, '=' * 5))
        print(str(item))
        print("="*15)
        return self

    def update(self, id=None, title=None, context=None):
        print(id, title, context)
        for item in self._todoList:
            if str(item.id) == str(id):
                print('find!', item)
                item.title = title or item.title
                item.context = context or item.context
        return self

    def save(self):
        print('{} save {}'.format('='*10, '='*10))
        with open(self._filepath, 'w') as f:
            f.write(str(self))
        print(str(self))
        print('='*10 + '\n\n')
        return self

    def filter(self, func_filter, *args, **kwargs):
        return func_filter(self._todoList[:], *args, **kwargs)

    def delete(self, items):
        print("="*10, " delete ", "="*10)
        print(set(self._todoList))
        print(set(items))
        self._todoList = list(set(self._todoList) - set(items))
        print(self._todoList)
        return self

    def json(self):
        return [item.json() for item in self._todoList]

    def __str__(self):
        return '{}\n{}'.format('{}'.format('\t'.join(self._keys)), ''.join([str(item) for item in self._todoList]))

class TodoListItem(object):
    def __init__(self, id=None, title=None, context=None, **kwargs):
        assert title
        assert context

        if not id:
            self._id = datetime.now().timestamp()
        else:
            self._id = id
        self.title = title
        self.context = context

    @property
    def id(self):
        return self._id

    def json(self):
        return dict({'id': self._id, 'title': self.title, 'context': self.context})

    def __str__(self):
        return '{}\t{}\t{}\n'.format(self._id, self.title, self.context)

    def __repr__(self):
        return 'TodoListItem: {}\n'.format(str(dict({'id': self._id, 'title': self.title, 'context': self.context})))
