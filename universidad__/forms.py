from django import forms
from .models import Departamento, Curso, Empleado, Estudiante, Profesor

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre_departamento']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre_curso', 'codigo_curso', 'departamento']

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'num_identificacion', 'correo', 'telefono']

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre_estudiante', 'apellido_estudiante', 'fecha_nacimiento', 'genero', 'correo_estudiante', 'telefono', 'direccion']

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre_profesor', 'apellido_profesor', 'correo_profesor', 'telefono']
