import time

def hora():
    Hora = time.strftime("%I:%M:%S:%p")
    print ("Hora actual=", Hora,end="\r",)
    

if __name__ == '__main__':
    try:
        while True:
            hora()
    
    except KeyboardInterrupt:
        Salir = input("¿Desea salir del programa? (s/n): ")
        if Salir.lower() == 's':
            print("Saliendo del programa.")
        
        else:
            print("Opción no válida. Continuando con el programa.")
