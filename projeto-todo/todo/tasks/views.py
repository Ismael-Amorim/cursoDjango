# toda view precisa receber um request como argumento
# dois passos que devem ser seguidos
# request como argumento, pra saber é é get ou post que o usuario esta acessando
# sempre retornar algo
# toda view é chamada pelo nome
# parametro padrao sempre request e depois o template
# nao colocar virgula no final do return

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import TaskForm


from .models import Task


# precisa chamar as tasks do banco pro template, vai chamar primeiro o model


def tasklist(request):
    tasks = Task.objects.all().order_by('-created_at')  # pegando tudo Task do banco
    return render(request, 'tasks/list.html', {'tasks': tasks})


def taskView(request, id):
    # argumento pega primeiro o model(Task) e depois o id(pk)
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})


def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})


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


def helloworld(request):
    return HttpResponse('Hello World')


def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})
