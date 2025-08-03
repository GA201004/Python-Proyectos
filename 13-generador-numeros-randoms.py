import random
import os
def clear_console():
    """Borra la consola detectando el sistema operativo."""
    os_name = os.name
    if os_name == 'posix':  # macOS, Linux
        os.system('clear')
    elif os_name == 'nt':  # Windows
        os.system('cls')

print("Bienvenido al Generador de Números Aleatorios")
print("----------------------------------")
while True:
    try:
         entrada_numero=  input ("Escriba un Numero:")
         rango_maximo= int (entrada_numero)
         print(f"Rango establecido: del 1 a {rango_maximo}\n")
         print("----------------------------------")
         break
       
    except ValueError:
        print ("¡Error! La entrada no es un número válido. Por favor, inténtelo de nuevo.")
        print("----------------------------------")
numeros_usados=set()
while True:
    if len(numeros_usados) >= rango_maximo:
         print("¡Todos los números posibles ya han sido generados!")
         print("----------------------------------")
         break
    while True:
           numero_aleatorio= random.randint(1,rango_maximo)
           if  numero_aleatorio not in numeros_usados:
               numeros_usados.add(numero_aleatorio)
               break
    clear_console()
    print(f"El Numero Generado es: {numero_aleatorio}")
    print(f"Números restantes por generar: {rango_maximo - len   (numeros_usados)}")
    print("----------------------------------")
            # Pide la respuesta y la convierte a minúsculas 
    respuesta= input ("Quiere generar otro numero (s/n):\n").lower()
    print("----------------------------------")
    if respuesta == 's':
      # Esta línea es opcional, pero hace el código más claro.
        continue 
    elif respuesta == 'n':
        print("¡Gracias por jugar! Adiós.")
        break
        # La palabra clave 'break' detiene este bucle y finaliza eprograma.
    else:
        # Si la respuesta no es 's' ni 'n', se lo informamos al usuario.
        print("Opción no válida. Por favor, escriba 's' o 'n'.")
        
    