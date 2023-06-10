from rest_framework import viewsets
from clientes.models import Clientes
from .serializers import ClienteSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClienteSerializer