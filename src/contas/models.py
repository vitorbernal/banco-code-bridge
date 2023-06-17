from django.db import models

class Conta(models.Model):
    cliente = models.ForeignKey('clientes.Clientes', null=True, on_delete=models.SET_NULL, related_name='contas')
    saldo = models.DecimalField('saldo do cliente', max_digits=12, decimal_places=2, default=0)
    data_abertura = models.DateTimeField(auto_now_add=True, null=False)
    
    def depositar(self,valor):
        self.saldo += valor
        self.save()

    def debitar(self,valor):
        self.saldo -= valor
        self.save()    

    def __str__(self):
        return f'{self.cliente} - R${self.saldo}'   
