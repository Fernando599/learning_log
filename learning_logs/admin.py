from django.contrib import admin
from learning_logs import models

@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_date',)
    search_fields = ('text',)
