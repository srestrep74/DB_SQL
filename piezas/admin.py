from django.contrib import admin

# Register your models here.
from .models import coleccionista
admin.site.register(coleccionista)

from .models import compra
admin.site.register(compra)

