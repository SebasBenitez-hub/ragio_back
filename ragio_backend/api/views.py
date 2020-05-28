from rest_framework import generics, filters
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import Servicio, Act, Colab, Cliente, ActDiarias
from .serializers import ServicioSerializers, ActSerializers, ColabSerializers, ClienteSerializers, ActDiariasSerializers

# Create your views here.

class ColabList(generics.ListCreateAPIView):
    filter_backends = [filters.SearchFilter,]
    search_fields = ['user__username']
    queryset = Colab.objects.all()
    serializer_class = ColabSerializers

class ClienteList(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializers

class ServicioList(generics.ListCreateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializers

class ActList(generics.ListCreateAPIView):
    search_fields = ['servicio__id']
    filter_backends = (filters.SearchFilter,)
    queryset = Act.objects.all()
    serializer_class = ActSerializers

class ActDiariasList(generics.ListCreateAPIView):
    queryset = ActDiarias.objects.all()
    serializer_class = ActDiariasSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['colaborador__nombreColab', 'cliente__nombreFiscal']
    filter_fields = ['fecha']