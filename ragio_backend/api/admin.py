from django.contrib import admin
from .models import Servicio, Act, Colab, Cliente,ActDiarias

# Register your models here.
@admin.register(Act)
class ActAdmin(admin.ModelAdmin):
    list_display = ('servicio','nombreActividad')
    ordering = ('servicio',)
    search_fields = ('nombreActividad','servicio__nombreServicio')
    list_per_page = 10

@admin.register(Colab)
class ColabAdmin(admin.ModelAdmin):
    list_display = ('nombreColab','user')
    ordering = ('nombreColab',)
    search_fields = ('nombreColab','user__username')
    list_per_page = 10

@admin.register(ActDiarias)
class ActDiariaAdmin(admin.ModelAdmin):
    list_display = ('servicio','actividad','colaborador','cliente','fecha')
    ordering = ('fecha',)
    search_fields = ('actividad__nombreActividad','fecha')
    list_per_page = 10

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombreFiscal', 'nombreComercial', 'poblacion', 'rfc')
    ordering = ('nombreFiscal',)
    search_fields = ('nombreFiscal', 'nombreComercial')
    list_per_page = 10

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombreServicio',)
    ordering = ('nombreServicio',)
    search_fields = ('nombreServicio',)
    list_per_page = 10