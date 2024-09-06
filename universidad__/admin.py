from django.contrib import admin
from .models import Departamento, Curso, Empleado, Estudiante, Profesor

admin.site.register(Departamento)
admin.site.register(Curso)
admin.site.register(Empleado)
admin.site.register(Estudiante)
admin.site.register(Profesor)
