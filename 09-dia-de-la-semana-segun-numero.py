dia_de_la_semana=[0,1,2,3,4,5,6,7]
dia=int(input("Ingrese un numero del 1 a 7:"))


if dia_de_la_semana[1]== dia:
      print ("El numero 1 pertence al dia Lunes")          
elif dia_de_la_semana [2]== dia:
        print ("El numero 2 pertence al dia Martes")
elif dia_de_la_semana [3]== dia:
        print ("El numero 3 pertence al dia Miercoles")
elif dia_de_la_semana [4]== dia:
        print ("El numero 4 pertence al dia Jueves")
elif dia_de_la_semana [5]== dia:                              
        print ("El numero 5 pertence al dia Viernes")
elif dia_de_la_semana [6]== dia:
        print ("El numero 6 pertence al dia Sabado")
elif dia_de_la_semana [7]== dia:
        print ("El numero 7 pertence al dia Domingo")        
elif dia_de_la_semana [0]==dia:
        print ("El numero 0 no corresponde a ningun dia de la semana")
else:
        print ("El numero no corresponde a ningun dia de la semana, vuelva a intentar")