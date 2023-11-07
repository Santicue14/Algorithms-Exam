import csv
from mensajes import *

class Alumno:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Alumnos:
    def __init__(self):
        self.alumnos = []

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def cargar_alumnos(self, archivo):
        try :
            with open(archivo) as arch:
                reader = csv.reader(arch,delimiter=";")
                next(reader)
                mensajes('Alumnos',[f"{'Nro':^5}{'Nombre':^25}{'Apellido':^25}"])    
                for pos, row in enumerate(reader):
                    nombre, apellido = row
                    print(f"{'':25s}{pos:^3}{nombre:^25}{apellido:^25}")
                    self.agregar_alumno(Alumno(nombre, apellido))
            return True            
       
        except FileNotFoundError:
            opcion = input(f"El archivo {archivo} no existe,\
Desea crearlo ? Si o No :").upper()
            if opcion == 'S':
                with open(archivo, mode='w', newline='') as arch:
                    writer = csv.writer(arch, delimiter=";")
                    writer.writerow(['Nombre', 'Apellido'])
                return True
            else:                
                return False
            
    def guardar_alumnos(self, archivo):
        with open(archivo, mode='w', newline='') as arch:
            writer = csv.writer(arch,delimiter=";")
            writer.writerow(['Nombre', 'Apellido'])
            for alumno in self.alumnos:
                writer.writerow([alumno.nombre, alumno.apellido])

# Nuevo metodo verifica si existe el nuevo alumno.
    def existe(self, reg_alumno):        
        for alumno in self.alumnos:
            if alumno.nombre == reg_alumno.nombre and alumno.apellido == reg_alumno.apellido:
                #Existe
                return False   
        return True

# Nuevo metodo para actualizar modificar un alumno
    def actualizar_alumno(self, index, alumno_nuevo):
        self.alumnos[index] = alumno_nuevo
        

# Nuevo metodo para eliminar  un alumno  
    def eliminar_alumno(self, index):
        self.alumnos.pop(index)
   

    

    
            
