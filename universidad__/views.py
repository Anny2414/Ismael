# universidad/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Departamento, Curso, Empleado, Estudiante, Profesor
from .forms import DepartamentoForm, CursoForm, EmpleadoForm, EstudianteForm, ProfesorForm

def listar_departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request, 'departamentos/departamentos.html', {'departamentos': departamentos})

def detalle_departamento(request, id_departamento):
    departamento = get_object_or_404(Departamento, id=id_departamento)
    return render(request, 'departamentos/detalle_departamento.html', {'departamento': departamento})

def crear_departamento(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_departamentos')
    else:
        form = DepartamentoForm()
    return render(request, 'departamentos/formulario_departamento.html', {'form': form})

def editar_departamento(request, id_departamento):
    departamento = get_object_or_404(Departamento, id=id_departamento)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            return redirect('detalle_departamento', id_departamento=id_departamento)
    else:
        form = DepartamentoForm(instance=departamento)
    return render(request, 'departamentos/formulario_departamento.html', {'form': form})
# Curso Views
def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'universidad/listar_cursos.html', {'cursos': cursos})

def detalle_curso(request, id_curso):
    curso = get_object_or_404(Curso, id=id_curso)
    return render(request, 'universidad/detalle_curso.html', {'curso': curso})

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'universidad/formulario_curso.html', {'form': form})

def editar_curso(request, id_curso):
    curso = get_object_or_404(Curso, id=id_curso)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('detalle_curso', id_curso=id_curso)
    else:
        form = CursoForm(instance=curso)
    return render(request, 'universidad/formulario_curso.html', {'form': form})

# Empleado Views
def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'universidad/listar_empleados.html', {'empleados': empleados})

def detalle_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id=id_empleado)
    return render(request, 'universidad/detalle_empleado.html', {'empleado': empleado})

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'universidad/formulario_empleado.html', {'form': form})

def editar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id=id_empleado)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('detalle_empleado', id_empleado=id_empleado)
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'universidad/formulario_empleado.html', {'form': form})

# Estudiante Views
def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'universidad/listar_estudiantes.html', {'estudiantes': estudiantes})

def detalle_estudiante(request, id_estudiante):
    estudiante = get_object_or_404(Estudiante, id=id_estudiante)
    return render(request, 'universidad/detalle_estudiante.html', {'estudiante': estudiante})

def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'universidad/formulario_estudiante.html', {'form': form})

def editar_estudiante(request, id_estudiante):
    estudiante = get_object_or_404(Estudiante, id=id_estudiante)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('detalle_estudiante', id_estudiante=id_estudiante)
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'universidad/formulario_estudiante.html', {'form': form})

# Profesor Views
def listar_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'universidad/listar_profesores.html', {'profesores': profesores})

def detalle_profesor(request, id_profesor):
    profesor = get_object_or_404(Profesor, id=id_profesor)
    return render(request, 'universidad/detalle_profesor.html', {'profesor': profesor})

def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_profesores')
    else:
        form = ProfesorForm()
    return render(request, 'universidad/formulario_profesor.html', {'form': form})

def editar_profesor(request, id_profesor):
    profesor = get_object_or_404(Profesor, id=id_profesor)
    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('detalle_profesor', id_profesor=id_profesor)
    else:
        form = ProfesorForm(instance=profesor)
    return render(request, 'universidad/formulario_profesor.html', {'form': form})
