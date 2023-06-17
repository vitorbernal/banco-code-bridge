from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from clientes.models import Clientes
from .serializers import ClienteSerializer, ContaSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClienteSerializer

    @action(detail=True, methods=['put'])
    def depositar(self, request, pk=None):
        cliente = self.get_object()

        serializer = ContaSerializer(
            data=request.data, instance=cliente
        )

        if serializer.is_valid():
            serializer.depositar()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        
    @action(detail=True, methods=['put'])
    def debitar(self, request, pk=None):
        cliente = self.get_object()

        serializer = ContaSerializer(
            data=request.data, instance=cliente
        )

        if serializer.is_valid():
            serializer.debitar()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)