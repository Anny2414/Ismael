from django.db import models

class Departamento(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nombre_departamento = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre_departamento

class Curso(models.Model):
    id_curso = models.CharField(primary_key=True ,max_length=20)
    nombre_curso = models.CharField(max_length=20)
    codigo_curso = models.IntegerField(unique=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, to_field='id_departamento')

    def __str__(self):
        return self.nombre_curso

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    num_identificacion = models.IntegerField(unique=True)
    correo = models.EmailField(max_length=80)
    telefono = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    nombre_estudiante = models.CharField(max_length=20)
    apellido_estudiante = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1)
    correo_estudiante = models.EmailField(max_length=200)
    telefono = models.CharField(max_length=11, unique=True)
    direccion = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nombre_estudiante} {self.apellido_estudiante}"

class Profesor(models.Model):
    id_profesor = models.AutoField(primary_key=True)
    nombre_profesor = models.CharField(max_length=20)
    apellido_profesor = models.CharField(max_length=20)
    correo_profesor = models.EmailField()
    telefono = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return f"{self.nombre_profesor} {self.apellido_profesor}"
