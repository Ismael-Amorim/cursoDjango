from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Task(models.Model):

    STATUS = (  # tipos pré definidos
        ('doing', 'Doing'),
        ('done', 'Done'),
    )

    # campos que vão ser inseridos na tabela
    # campo de caracteres (charfield) tem que ter o max_lenght
    title = models.CharField(max_length=255)
    # text é para textos maiores, não define tamanho
    description = models.TextField()
    done = models.CharField(  # pra saber o status da tarefa
        max_length=5,
        choices=STATUS,
    )

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # campo de data do django, cria automatico esse valor qunado for criado um valor no banco
    update_at = models.DateTimeField(auto_now=True)
    # cria automatico esse valor qunado for criado um valor no banco

    def __str__(self):
        return self.title
