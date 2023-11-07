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
        #Punto 3
        try:
            with open('alumnoseliminados.csv',mode='x') as arch: #Creo el archivo en modo 'x' para ver si ya está creado, si no es así,lo creo
                writer = csv.writer(arch,delimiter=';')
                writer.writerow(['Nombre','Apellido']) #Pongo las columnas
        except FileExistsError: #Si el archivo existe, paso de largo
            pass
        with open('alumnoseliminados.csv',mode='a') as arch: 
            cursor = csv.writer(arch,delimiter=';') #Con el archivo abierto
            alumno_eliminado = self.alumnos[index] #Tomo el alumno eliminado y lo guardo en una variable
            cursor.writerow([alumno_eliminado.nombre,alumno_eliminado.apellido]) #Tomo nombre y apellido del alumno_eliminado y lo guardo
        self.alumnos.pop(index) #Además borro el alumno, tal como ya estaba antes
#Punto 4
def log_de_modificacion(accion,alumno):
    try:
        with open('log_de_modificacion.csv',mode='x',encoding='utf-8') as arch: #Creo el archivo en modo 'x' para ver si ya está creado, si no es así,lo creo
            writer = csv.writer(arch,delimiter=';')
            writer.writerow(['Nombre','Apellido','Opción']) #Pongo las columnas
    except FileExistsError: #Si el archivo existe, paso de largo
        pass
    if accion == 'e': #Evalúo cual es la accion que se hizo
        que_se_hizo = 'Se eliminó'
    elif accion == 'm':
        que_se_hizo = 'Se modificó'
    with open('log_de_modificacion.csv',mode='a',encoding='utf-8') as arch: #Encoding uft-8 para que ponga bien las tildes
        cursor = csv.writer(arch,delimiter=';') #Con el archivo abierto
        cursor.writerow([alumno.nombre,alumno.apellido,que_se_hizo]) #Tomo nombre y apellido del alumno, además de la accion y lo guardo


    

    
            
