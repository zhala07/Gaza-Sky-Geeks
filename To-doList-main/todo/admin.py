from django.contrib import admin
from todo.models import Note, Type

admin.site.register(Note)
admin.site.register(Type)