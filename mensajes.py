
def mensajes(titulo,mensaje,m_opcion=""):
    largo_menu = len(titulo)    
    superior = (60 - largo_menu -2 )//2  
    if len(titulo) > 59:
        print("Mensaje, El titulo no debe superar los 59 caracteres")
        return
        
    if len(mensaje) == 1:
        print(f"\n{' ':20s}{titulo} {'-' * (superior*2)}")
    else:
        print(f"\n{' ':20s}{'-' * superior} {titulo} {'-' * superior}")
   
    elementos = len(mensaje)    
    for i in range(elementos):        
        if elementos == 1:
            print(f"{' ':20s}{str(mensaje[i]):^60s}")
        else:
            print(f"{' ':25s}{mensaje[i]}")  
    if m_opcion =="":
        print(f"{' ':20s}{'-' * 60}\n{' ':20s}{m_opcion}")
    else:
        return input(f"{' ':20s}{'-' * 60}\n{' ':20s}{m_opcion}")