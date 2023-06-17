from rest_framework import serializers
from clientes.models import Clientes

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'



class ContaSerializer(serializers.Serializer):
    valor = serializers.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        fields = ('valor',)

    def depositar(self):
        self.conta = self.instance.contas.first()
        self.conta.depositar(self.validated_data['valor'])

    def debitar(self):
        self.conta = self.instance.contas.first()
        self.conta.debitar(self.validated_data['valor'])    

    def to_representation(self, instance):
        return {'saldo': self.conta.saldo}            