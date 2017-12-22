from django.db import models

# Create your models here.

STATUS = (
    ('novo', 'Novo'),
    ('na_fila', 'Na fila'),
    ('em_processo', 'Em Processo'),
    ('processado', 'Processado'),
    ('falhou', 'Falhou'),
)


class Email(models.Model):

    email = models.EmailField()
    status = models.CharField(max_length=100, choices=STATUS, default='novo')
    fui = models.BooleanField(default=False)
    resultado = models.TextField(default=None, blank=True, null=True)