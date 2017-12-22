from django.contrib import admin

# Register your models here.

from aplicacao.models import Email

from aplicacao.tasks import consulta_no_havebeenpwned

class EmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'status', 'fui', 'resultado',)
    readonly_fields = ['status', 'resultado', 'fui']
    actions = ['poem_na_fila']

    def poem_na_fila(self, request, queryset):
        queryset.update(status='na_fila')
        for model_obj in queryset.all():
            consulta_no_havebeenpwned.delay(model_obj.id)

    poem_na_fila.short_description = "Poem na fila"



admin.site.register(Email, EmailAdmin)