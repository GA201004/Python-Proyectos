dia_de_la_semana={
    1:"Lunes"
    ,2:"Martes"
    ,3:"Miércoles"
    ,4:"Jueves"
    ,5:"Viernes"
    ,6:"Sábado"
    ,7:"Domingo"
}

while True:
   try:
       entrada = input("Ingrese un numero del 1 a 7:")
       dia = int(entrada)
       if dia in dia_de_la_semana:
           print("El numero", dia, "pertence al dia:", dia_de_la_semana[dia])
           break
       else:
           print("Número no válido. Por favor, ingrese un número del 1 al 7.")
           
           continue
   except ValueError:
       print("Entrada no válida. Por favor, ingrese un número del 1 al 7.")
       
