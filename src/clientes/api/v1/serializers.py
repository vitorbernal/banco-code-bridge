from rest_framework import serializers
from clientes.models import Clientes

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'