from django.contrib import admin # esse eh generico do django
from petshop.models import Animal, Dono, Funcionario, Atendimento # acabamos de criar

class AnimalAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'idade', 'dono']


class DonoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']

class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ['id', 'animal', 'dia_da_consulta', 'consultado_por', 'display_obs_encurtada', 'nova_coluna_estatica']

    def display_obs_encurtada(self, obj):
        return obj.observacao[:30]
    display_obs_encurtada.short_description = "observacao enc"

    def nova_coluna_estatica(self, obj):
        return 42
    nova_coluna_estatica.short_description = "Numero"

admin.site.register(Animal, AnimalAdmin)
admin.site.register(Dono, DonoAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Atendimento, AtendimentoAdmin)
