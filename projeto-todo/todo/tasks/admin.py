from django.contrib import admin

# Register your models here.

# grupo da tarefa, ou seja, como se fosse uma tabela nova no mysql
from .models import Task

admin.site.register(Task)
