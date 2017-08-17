from django.db import models

class Dono(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Animal(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    dono = models.ForeignKey(Dono, default=1)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Atendimento(models.Model):
    animal = models.ForeignKey(Animal)
    dia_da_consulta = models.DateField(auto_now_add=True)
    consultado_por = models.ForeignKey(Funcionario)
    observacao = models.TextField(default='')


    def __str__(self):
        return "{} - {}".format(self.animal, self.dia_da_consulta)
