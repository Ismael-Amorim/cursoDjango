# toda view precisa receber um request como argumento
# dois passos que devem ser seguidos
# request como argumento, pra saber é é get ou post que o usuario esta acessando
# sempre retornar algo
# toda view é chamada pelo nome
# parametro padrao sempre request e depois o template
# nao colocar virgula no final do return

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import TaskForm
from django.contrib import messages
import datetime


from .models import Task


# precisa chamar as tasks do banco pro template, vai chamar primeiro o model

@login_required
def tasklist(request):

    search = request.GET.get('search')
    filter = request.GET.get('filter')
    tasksDoneRecently = Task.objects.filter(done='done', update_at__gt=datetime.datetime.now(
    )-datetime.timedelta(days=30), user=request.user).count()
    tasksDone = Task.objects.filter(done='done', user=request.user).count()
    TasksDoing = Task.objects.filter(done='doing', user=request.user).count()
    if search:

        tasks = Task.objects.filter(title__icontains=search, user=request.user)

    elif filter:

        tasks = Task.objects.filter(done=filter, user=request.user)

    else:

        tasks_list = Task.objects.all().order_by(
            '-created_at').filter(user=request.user)  # pegando tudo Task do banco

        paginator = Paginator(tasks_list, 3)

        page = request.GET.get('page')

        tasks = paginator.get_page(page)

    return render(request, 'tasks/list.html', {'tasks': tasks, 'tasksrecently': tasksDoneRecently, 'tasksdone': tasksDone, 'tasksdoing': TasksDoing})


@login_required
def taskView(request, id):
    # argumento pega primeiro o model(Task) e depois o id(pk)
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})


@login_required
def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.user = request.user
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})


@login_required
def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if (request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)

        if (form.is_valid()):
            task.save()
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form': form, 'task': task})
    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'task': task})


@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso!')

    return redirect('/')


@login_required
def changeStatus(request, id):
    task = get_object_or_404(Task, pk=id)

    if (task.done == 'doing'):
        task.done = 'done'
    else:
        task.done = 'doing'

    task.save()

    return redirect('/')


def helloworld(request):
    return HttpResponse('Hello World')


def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})
