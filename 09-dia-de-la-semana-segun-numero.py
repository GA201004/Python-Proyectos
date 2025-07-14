dia_de_la_semana=[0,1,2,3,4,5,6,7]
dia=int(input("Ingrese un numero del 1 a 7:"))

while True:
        if dia_de_la_semana[1]== dia:
            print ("El numero 1 pertence al dia Lunes")
            break
        elif dia_de_la_semana [2]== dia:
               print ("El numero 2 pertence al dia Martes")
               break
        elif dia_de_la_semana [3]== dia:
               print ("El numero 3 pertence al dia Miercoles")
               break
        elif dia_de_la_semana [4]== dia:
               print ("El numero 4 pertence al dia Jueves")
               break
        elif dia_de_la_semana [5]== dia:
               print ("El numero 5 pertence al dia Viernes")
               break
        elif dia_de_la_semana [6]== dia:
               print ("El numero 6 pertence al dia Sabado")
               break
        elif dia_de_la_semana [7]== dia:
               print ("El numero 7 pertence al dia Domingo")
               break
        elif dia < 1 or dia > 7:
               if dia == 0:
                   print("El Numero 0 no corresponde a ningun dia de la semana, vuelva a intentar: ")
                   wlay = input("¿Desea volver a intentarlo? (s/n): ")
                   if wlay.lower() == 'n':
                       print("Saliendo del programa. ¡Hasta luego!")
                       break
                   else:
                       dia = int(input("Por favor ingrese un numero valido del 1 al 7: "))
               else:
                   print("Por favor ingrese un numero valido.")
                  
                   if dia > 7:
                     wlay = input("¿Desea volver a intentarlo? (s/n): ")
                     if wlay.lower() == 'n':
                        print("Saliendo del programa. ¡Hasta luego!")
                        break
                     else:
                         dia = int(input("Por favor ingrese un numero valido del 1 al 7: "))
        else:
               print ("El numero no corresponde a ningun dia de la semana, vuelva a intentar")
               break