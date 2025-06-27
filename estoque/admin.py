from django.contrib import admin

from django.contrib import admin
from import_export.admin import ExportMixin
from .models import Material, Movimentacao

@admin.register(Material)
class MaterialAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('nome', 'quantidade', 'validade', 'descartado')
    search_fields = ('nome',)
    list_filter = ('descartado',)

@admin.register(Movimentacao)
class MovimentacaoAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('material', 'tipo', 'quantidade', 'em_uso', 'professor_responsavel', 'estoque_minimo', 'estoque_maximo', 'data')
    list_filter = ('tipo',)
    search_fields = ('material__nome',)
