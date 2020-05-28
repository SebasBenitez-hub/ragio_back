from rest_framework import serializers
from .models import Servicio, Act, Colab, Cliente, ActDiarias


class ColabSerializers(serializers.ModelSerializer):
    class Meta:
        model = Colab
        fields = ('id','user','nombreColab','tituloProf','correoColab','telefonoColab')

class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields= ('id','nombreFiscal', 'nombreComercial','poblacion','estado','pais','rfc')

class ServicioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ('id','nombreServicio')

class ActSerializers(serializers.ModelSerializer):
    servicio_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Act
        fields = ('id','servicio','servicio_id','nombreActividad')
        depth = 1

class ActDiariasSerializers(serializers.ModelSerializer):
    cliente_id = serializers.IntegerField(write_only=True)
    colaborador_id = serializers.IntegerField(write_only=True)
    servicio_id = serializers.IntegerField(write_only=True)
    actividad_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ActDiarias
        fields = ('id','cliente','cliente_id','colaborador','colaborador_id','servicio','servicio_id','actividad','actividad_id','fecha','desdeHora','hastaHora','observacionAdicional','porcentajeAvance')
        depth = 1