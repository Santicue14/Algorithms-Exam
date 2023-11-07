import csv
from datetime import date

class Presentismo:
    def __init__(self, fecha, alumno, estado):
        '''fecha = fecha actual,
           (apellido + nombre) del arch alumnos.cvs,
           estado = S, N'''       
        self.fecha = fecha
        self.alumno = alumno
        self.estado = estado
 
class Presentismo_dia:
    def __init__(self):
        self.pres_dia = []
        self.alumnos = []

    def agregar_presentismo(self, pres_alumno):
        self.pres_dia.append(pres_alumno)
    
    def guardar_presentismo(self, archivo):
        with open(archivo, mode='w', newline='') as arch:
            writer = csv.writer(arch,delimiter=";")
            writer.writerow(['Fecha', 'Alumno','Presentismo'])
            for pres in self.pres_dia:
                writer.writerow([pres.fecha, pres.alumno,pres.estado])

    def cargar_presentismo(self, archivo):
        try :
            with open(archivo) as arch:
                reader = csv.reader(arch,delimiter=";")
                next(reader)
                for fecha, alumno, estado in reader:
                    #nombre, apellido= row
                    self.agregar_presentismo(Presentismo(fecha, alumno, estado))
            return True
        except FileNotFoundError:
            opcion = input(f"El archivo {archivo} no existe, Desea crearlo ? Si o No :").upper()
            if opcion == 'S':
                with open(archivo, mode='w', newline='') as arch:
                    writer = csv.writer(arch, delimiter=";")
                    writer.writerow(['Fecha', 'Alumno','Presentismo'])
                return True
            else:
                return False
    
    def cargar_alumnos(self, archivo):
        try :
            with open(archivo) as arch:
                reader = csv.reader(arch,delimiter=";")
                next(reader)
                for nombre, apellido in reader:                   
                    self.alumnos.append(apellido +" "+  nombre)
            return True
        except FileNotFoundError:
            print(f"El archivo {archivo} no existe, ingrese a la opcion 1 del menú para crearlo")
            return False

# Nueva metodo devolver, devuelve en una lista con todos los registros de presentismo para luego poder manipularlo, en los listados            
    def devolver(self):
        lista= []
        for pres in self.pres_dia:
            lista.append([pres.fecha, pres.alumno,pres.estado])
        return lista     

# Punto 1 función
def actualizar_en_presen(archivo_presen, alumno_viejo, alumno_nuevo):
    with open(archivo_presen, mode="r") as arch: #Abro el archivo_presen en modo lectura
        filas_de_presentismo = list(csv.reader(arch, delimiter=';')) #Listo las filas del archivo para luego recorrerlas
        
    for fila in filas_de_presentismo: #Bucle que recorre todas las filas de presentismo
        fecha, alumno, presencia = fila #Agarro cada columna de la fila y la almaceno en fecha,alumno, y si asistió o no
        if alumno == f'{alumno_viejo.apellido} {alumno_viejo.nombre}': #Busca el alumno viejo obteniendo los datos desde principal.py
            fila[1] = f'{alumno_nuevo.apellido} {alumno_nuevo.nombre}'#Si es el alumno le cambia los atributos por los del nuevo Alumno generado

    with open(archivo_presen, mode='w', newline='') as arch: #Vuelvo a abrir el archivo pero en modo escritura
        cursor = csv.writer(arch, delimiter=';')
        cursor.writerow([fecha, alumno_nuevo,presencia]) #Modifico las filas nuevas
        cursor.writerows(filas_de_presentismo)  #Luego de modificar las filas por el alumno nuevo continua con los otros valores
