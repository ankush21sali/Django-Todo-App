from django.db import models

# Create your models here.
class Todo_List(models.Model):
    todo_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title