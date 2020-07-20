from django.db import models

# Create your models here.

class TodoListItem(models.Model):
    # id
    todo = models.TextField()
    is_checked = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    @property
    def json(self):
        return dict({
            'id': self.id,
            'todo': self.todo,
            'is_checked': self.is_checked,
            'create_date': self.create_date,
            'update_date': self.update_date
        })

