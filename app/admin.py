from django.contrib import admin
from .models import Reservas, Huespedes, Usuarios

# Register your models here.

admin.site.register(Reservas)
admin.site.register(Huespedes)
admin.site.register(Usuarios)
