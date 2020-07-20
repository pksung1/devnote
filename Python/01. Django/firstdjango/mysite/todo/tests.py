from django.test import TestCase

# Create your tests here.
from .models import TodoListItem


class TodoListItemModelTest(TestCase):
    def test_add_item(self):
        item = TodoListItem(todo="")
        self.assertIs(item.todo, "", "todo_data_not_equal")
        self.assertIs(item.is_checked, False, "is_checked_not_equal")

    def test_add_item_none(self):
        # item = TodoListItem(todo=None)
        # self.assertIs(item.todo, "", "todo_data_none_checked")
        pass
