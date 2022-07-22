from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models import TextField


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    local = models.CharField(null=True, max_length=50)
    descricao = models.TextField(blank=True, null=True)
    date_evento = models.DateTimeField(verbose_name='Data do evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.local

    def get_data_evento(self):
        return self.date_evento.strftime('%d/%m/%Y %H:%M Horas')

    def get_data_input_evento(self):
        return self.date_evento.strftime('%Y-%m-%dT%H:%M')


