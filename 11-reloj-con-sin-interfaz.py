import time

def hora():
    Hora = time.strftime("%I:%M:%S:%p")
    print ("Hora actual:", Hora)
    

if __name__ == '__main__':
    try:
        while True:
            hora()
            time.sleep(1)
            
    except KeyboardInterrupt:
        Salir = input("¿Desea salir del programa? (s/n): ")
        if Salir.lower() == 's':
            print("Saliendo del programa.")
        else:
            print("Continuando con el programa.")
