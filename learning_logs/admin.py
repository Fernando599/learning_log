from django.contrib import admin
from learning_logs import models

@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date')
    search_fields = ('name',)

@admin.register(models.Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'created_date', 'resumo_texto')

    def resumo_texto(self, obj):
        return obj.text[:50] + "..." if len(obj.text) > 50 else obj.text
    resumo_texto.short_description = "Text"
