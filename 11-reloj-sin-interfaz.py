import time

def hora():
    Hora = time.strftime("%I:%M:%S:%p")
    print ("Hora actual=", Hora,end="\r",)

if __name__ == '__main__':
    print("------Reloj sin interfaz gráfica------")
    print("Presione Ctrl+C para detener el reloj.")
    ejecutando = True
    while True:
        
        try:
            while ejecutando:
                  hora()
                  time.sleep(1)
            
        except KeyboardInterrupt:
            Salir = input("¿Desea salir del programa? (s/n): ")
        if Salir.lower() == 's':
            print("Saliendo del programa.")
            ejecutando = False
            break

        else:
            print("------Continuando con el reloj------")
