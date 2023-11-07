
'''CRUD ALUMNOS DEL PROGRAMA PRESENTISMO
pass rar algoritmosyprogramacion2023
* Hasta la clase 9 el programa presentismo contaba de 3 archivos

principal.py
alumnos_para_clase.py
presentimos_para_clase.py


Hasta ahora el programa contenia 3 archivos principales y dos funcionalidades.

1. El programa consiste en la carga de alumnos y en la carga del presentismo de estos alumnos.


principal.py

Importa las clases y modulos de los archivos alumnos_para_clase, presentismo_para_clase y mensajes.

Este archivo es el centro funcional del programa unifica las clases y modulos por medio de un menu principal
y funciones para la carga de datos.

Menu principal
    1- Cargar Alumnos
    2- Tomar presentismo
    3- Salir

Funciones:
    alta_alum (utilizando las clases y metodos de alumnos_para_clase.py, carga, lista y agrega nuevos alumnos.
              Atención realiza primero la lectura del archivo alummos.csv para luego escribir nuevamente  los datos
              en el archivo porque se abre en modo W creacion cuando se guarda.)
    
    presen    (utilizando las clases y metodos de presentimos_para_clase.py, carga los alumnos con el apellido y nombre concatenado,
               toma el presentismo.
              Atención realiza primero la lectura del archivo presentismo.csv para luego escribir nuevamente  los datos
              en el archivo porque se abre en modo W creacion cuando se guarda.)
    

2. La carga de alumnos en archivo alummos.csv.

alumnos_para_clase.py

Contiene el TDA alumnos, con las clases:

class Alumno 
    Metodo constructor
        nombre
        apellido

class Alumnos
    Metodo constructor
        alumnos = []

    Metodos
        agregar_alumno  (agrega a la lista alumnos, el objeto Alumno)
        guardar_alumnos (Abre el archivo alummos.csv en modo w, escribe el encabezado y agrega la lista de alumnos cargados)
        cargar_alumnos  (Abre el archivo alummos.csv en modo r y muestra el listado de alumnos
                         guardados en el archivo y los carga en la lista alumnos de la clase para una mejor manipulacion.
                         en el caso de que el archivo alummos.csv no exista lo crea y escribe el encabezado )
                         
3. La carga del presentismo diaria de los alumnos dados de alta, que se encontraban en el archivo alummos.csv, el presentismo se guarda en
el archivo presentismo.csv. (presentimos_para_clase.py)

presentimos_para_clase.py


Contiene el TDA presentismo, y las clases:

class Presentismo:
    Metodo constructor
        fecha
        alumno 
        estado

class Presentismo_dia:
    Metodo constructor
        pres_dia = []
        alumnos = []
    
    Metodos
        agregar_presentismo (agrega a la lista pres_dia, el objeto Presentismo)
        guardar_presentismo (Abre el archivo presentismo.csv en modo w ,  escribe el encabezado y agrega la lista de presentismos cargados)
        cargar_presentismo  (Abre el archivo presentismo.csv en modo r y "NO muestra el listado de presentismos
                             guardados en el archivo " pero si los carga en la lista presentismos de la clase para una mejor manipulacion.
                             en el caso de que el archivo presentismo.csv no exista lo crea y escribe el encabezado )
        cargar_alumnos      (Abre el archivo alummos.csv en modo r los carga en la lista alumnos, pero concatena apellido + nombre y los guarda en
                             la lista alumnos de la clase Presentismo_dia
                             en el caso de que el archivo alummos.csv no exista muestra el aviso pero no lo crea )
        



Clase 10 CRUD 

Cambiaremos el menu y agregaremos las siguientes funcionalidades


1. Debera realizar los siguientes cambios en el Menu

                    ---------------------- MENÚ PRINCIPAL ----------------------
                         1- Gestión de Alumnos
                         2- Gestión de Presentismo
                         3- Salir
                    ------------------------------------------------------------
                    SELECCIONE UNA OPCIÓN: 

2. Agregue el submenu para la opcion 1- Gestión de Alumnos

                    -------------------- Gestión de Alumnos --------------------
                         1- Cargar
                         2- Listar
                         3- Modificar
                         4- Eliminar
                         5- Volver al menú principal
                    ------------------------------------------------------------
                    SELECCIONE UNA OPCIÓN:

3. Agregue el submenu para la opcion 2- Gestión de Presentismo

                    ------------------ Gestión de Presentismo ------------------
                         1- Cargar
                         2- Listar Todo
                         3- Listar por fecha
                         4- Listar por Alumno
                         5- Volver al menú principal
                    ------------------------------------------------------------
                    SELECCIONE UNA OPCIÓN:


Detalle de los Submenu

Menu principal
    1- Gestion Alumnos
        1. Cargar
        La carga se sigue realizando de la misma manera pero se debe agregar 
        la funcionalidad para controlar si existe un alumno con el mismo nombre y apellido si esto pasa
        debe avisar que el alumno ya existe y no guardara el alumno.
        
        2. Listar
        Muestra todos los registros de alumnos cargados
        
        3. Modificar
        Muestra el listado de alumnos enumerados desde el numero 0 y solicita el nro de alumno a modificar
        verificar si la numeracion existe y proceder a solicitar nuevamente el nombre y apellido.
        Luego guarda los datos en el archivo.       
        
            Para parcial. (Cuando modifique el nombre de un alumno debera modificar tambien el archivo de presentismo donde aparezca el ese alumno
            recuerde el nombre del alumno se forma con el apellido + nombre)
            Entonces si se modifica un alumno , ya sea nombre o apellido existente debera modificarse el nombre en el archivo presentismo.
            
            Explicacion de las claves primarias de id 
     
        4. Eliminar
        Muestra el listado de alumnos enumerados desde el numero 0 y solicita el nro de alumno a eliminar
        verificar si la numeracion existe y proceder a eliminar el alumno.
        Luego guarda los datos en el archivo.
        
               
        5. Volver al menu principal


Menu principal
    2- Gestion presentismo    
        1. Tomar presentismo
           Realiza la carga del presentismo, por medio de un TDA  deberá obtener los nombres de los alumnos desde el archivo alumnos.cvs,
           deberá cargar el presentismo con los siguientes datos (fecha, apellido + nombre del alumno en archivo, estado(S  presente / N ausente)
           (item resuelto)
        
        2. Listar Todo
           Muestra todos los registros del archivo presentismo.
           
        3. Listar por fecha
           Solicita la fecha en formato AAAA-MM-DD para mostrar todos los registros de presentismo de ese dia
        
        4. Listar por Alumno
           Solicita el Apellido y Nombre para mostrar todos los registros de ese alumno.
        
        5. Volver al menu principal        

Menu principal
    3- Salir
       Finaliza el programa



Nuevas funciones y metodos de los archivos

principal.py
Funciones:
    listar             (El listado estaba resuelta en el metodo de la cargar_alumnos de la Clase Alumnos)
    modif_elim_alumno  (Esta funcion modifica o elimina el alumno depende del parametro accion: m Modifica el alumno y e Elimina
                        el alumno y guarda el cambio)
                        
                        Primero Muestra el listado de alumnos enumerados desde el numero 0 y solicita el nro de alumno a modificar
                        verificar si la numeracion existe y proceder a solicitar nuevamente el nombre y apellido.
                        Luego guarda los datos en el archivo

    listar_pres        (Esta funcion centraliza los 3 tipos de listado de presentismo, todo, por fecha y por alumno que discrimina por medio
                        del parametro accion con los valores 1,2,3 correlativamente )


alumnos_para_clase.py
    existe            (Posee un parametro reg_alumno (contiene el Apellido + nombre )y  Verifica si existe el Alumno en alumnos
                       si existe devuelve False)
    actualizar_alumno (Modifica el alumnos por medio del indice)
    eliminar_alumno   (Elimina el alumnos por medio del indice)
    

presentimos_para_clase.py
    devolver          (devuelve en una lista con todos los registros de presentismo para luego poder manipularlo, en los listados)            


'''


'''
PARA PARCIAL
1. Cuando modifique el nombre de un alumno debera modificar tambien el archivo de presentismo donde aparezca el ese alumno recuerde el nombre del alumno se forma con el apellido + nombre.
   Entonces si se modifica un alumno , ya sea nombre o apellido existente debera modificarse el nombre en el archivo presentismo en todas sus apariciones.

2. Cuando elimine un alumno debera elimnar todos los registros del alumno en el archivo presentismo.    

3. Guarde en otro archivo todos los registros eliminados.     

4. Genere archivo de Log de modificacion y eliminacion de registros guarde fecha y accion: modificacion o eliminacion y alumno comprometido.
    
    
    
'''

from alumnos_para_clase import *
from presentismo_para_clase import *
from mensajes import *


# Funciones para los alumnos

def alta_alum():    
    aper1 = False
    alumnos = Alumnos()
    aper1 = alumnos.cargar_alumnos('alumnos.csv')
    if aper1 == True:        
        while True:
            alumno = Alumno(input("\n                    Ingrese Nombre: ").capitalize(),
                            input("                    Ingrese Apellido: ").capitalize())
            # Nueva verificacion , valido si existe el nuevo alumno (nombre y apellido)
            if alumno.apellido != "" and alumno.nombre != "" and alumnos.existe(alumno):
                alumnos.agregar_alumno(alumno)
            else:
                print("\n                    Error faltan datos o el Alumno ya existe\n")              
            opcion = input("                    Desea seguir agregando alumnos ? Si o No :").upper()
            if opcion == 'N':    
                break
        alumnos.guardar_alumnos('alumnos.csv')        
        
# Funcion para listar alumnos
def listar():
    alumnos = Alumnos()
    alumnos.cargar_alumnos('alumnos.csv')
    input("\n                    Presione ENTER para volver")   

# Funcion que modifica o elimina el alumno el parametro accion m Modifica el alumno y e Elimina el alumno y guarda el cambio. 
def modif_elim_alumno(accion):
    # accion si es  m modifica y e elimina
    alumnos = Alumnos()
    aper1 = alumnos.cargar_alumnos('alumnos.csv')
    if aper1 == True:  
        tamano = len(alumnos.alumnos)-1
        correcto = False
        
        while True and tamano >-1:
            try:
                index=int(input(f"\n                    Ingrese el Nro de alumno 0 - {tamano} (x para salir): "))
                if index >=0 and index<=tamano:    
                    if accion.lower() == 'm': 
                        n_alumno = Alumno(input("\n                    Ingrese Nombre: ").capitalize(),
                                          input("                    Ingrese Apellido: ").capitalize())
                        if n_alumno.apellido != "" and n_alumno.nombre != "" and alumnos.existe(n_alumno):
                            alumno_antiguo = alumnos.alumnos[index]
                            alumnos.actualizar_alumno(index,n_alumno)
                            actualizar_en_presen('presentismo.csv',alumno_antiguo,n_alumno) #Llamo a la función cada vez que se modifique el alumno (la función está detallada en presentismo_para_clase.py)
                            correcto = True

                        else:
                            print("\n                    Error faltan datos o el Alumno ya existe\n")
                    
                    elif accion.lower() == 'e':
                        alumnos.eliminar_alumno(index)
                        correcto = True                    
                    break
            except ValueError:
                break
        if correcto:
            alumnos.guardar_alumnos('alumnos.csv')                                  
        input("\n                    Presione ENTER para volver") 


#Funciones para Presentismo
    
def presen():
    aper1 = False
    aper2 = False
    tomar_lista =  Presentismo_dia()
    aper1 = tomar_lista.cargar_alumnos('alumnos.csv')    
    if aper1 == True:
        aper2 = tomar_lista.cargar_presentismo('presentismo.csv')    
    if aper2 == True:   
        mensajes('Presentismo',[f"{'Fecha':^10}{'Alumno':^30}{'Si / No':^5}"])     
        fecha = str(date.today())
        
        for alum in tomar_lista.alumnos:
            while True:
                try:
                    estado_d = input(f"{'':25s}{fecha:^10}{alum:^30} ").upper()
                    if estado_d in 'SN':
                        presen = Presentismo(fecha,alum,estado_d)
                        tomar_lista.agregar_presentismo(presen)
                        break
                except Exception:
                    continue                  
        tomar_lista.guardar_presentismo('presentismo.csv')
        
def listar_pres(opcion):
    tomar_lista =  Presentismo_dia()
    tomar_lista.cargar_presentismo('presentismo.csv')
    listado =tomar_lista.devolver()    
    contador = 0
    largo = len(listado)
    registros = 0
    
    titulo=""
    if opcion == 1:
        consulta ="todo"
        titulo='Listado presentismo'
        #mensajes(titulo,[f"{'Fecha':^10}{'Alumno':^30}{'Si / No':^5}"])
    elif opcion==2:
        titulo='Listado presentismo por fecha'
        consulta =mensajes('Listado presentismo por fecha',["Ingrese la fecha a mostrar" ], "Ingrese AAAA-MM-DD: ") 
        #mensajes(titulo,[f"{'Fecha':^10}{'Alumno':^30}{'Si / No':^5}"])
    elif opcion==3:
        titulo='Listado presentismo por Alumno'
        consulta =mensajes('Listado presentismo por Alumno',["Ingrese el Alumno"], "Apellido Nombre: ")     
    mensajes(titulo,[f"{'Fecha':^10}{'Alumno':^30}{'Si / No':^5}"]) 
    for fecha,alumno,pres in listado:
        if consulta == fecha or consulta == alumno or consulta == 'todo':
            #if fecha == fecha_b:
            contador +=1
            registros +=1
            print(f"{' '*25}{fecha:^10}{alumno:^30}{pres:^5}")
            if contador == 10:
                mensajes('-',[f"Registro: {registros}/{largo} , Presione Enter para continuar"]," ")
                mensajes(titulo,[f"{'Fecha':^10}{'Alumno':^30}{'Si / No':^5}"])                       
                contador=0       
    if contador !=0:
        mensajes('-',[f"Registro: {registros}/{largo} , Presione Enter para continuar"]," ")
      

  

        
#inicio del programa


while True:
    op = mensajes('MENÚ PRINCIPAL',
                ["1- Gestión de Alumnos",
                 "2- Gestión de Presentismo",
                 "3- Salir"],
                 "SELECCIONE UNA OPCIÓN: ")
    print()
    if op == '1':
        while True:
            op_galum = mensajes('Gestión de Alumnos',
                    ["1- Cargar",
                     "2- Listar",
                     "3- Modificar",
                     "4- Eliminar",
                     "5- Volver al menú principal"],
                     "SELECCIONE UNA OPCIÓN: ")            
            if op_galum == '1':       
                alta_alum()
            elif op_galum == '2':
                listar()              
            elif op_galum == '3':      
                modif_elim_alumno('m')
            elif op_galum == '4':       
                modif_elim_alumno('e')                
            elif op_galum == '5':
                break
            
    elif op == '2':
        while True:
            op_gpres = mensajes('Gestión de Presentismo',
                    ["1- Cargar",
                     "2- Listar Todo",
                     "3- Listar por fecha",
                     "4- Listar por Alumno",
                     "5- Volver al menú principal"],
                     "SELECCIONE UNA OPCIÓN: ")
            if op_gpres == '1':  
                presen()
            elif op_gpres == '2':
                listar_pres(1)                
            elif op_gpres == '3':
                listar_pres(2)
            elif op_gpres == '4':       
                listar_pres(3)
            elif op_gpres == '5':
                break          
    elif op == '3':
        break

        