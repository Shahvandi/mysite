from django.contrib import admin
from .models import Message

# admin.site.register(Message)
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'unread', 'subject']
    list_editable = ['unread']