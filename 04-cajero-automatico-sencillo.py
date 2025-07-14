# 04-cajero-automatico-sencillo.py
# Este es un programa sencillo de cajero automático que permite realizar operaciones básicas como retiro, depósito,
# consulta de saldo y cambio de clave. El programa solicita al usuario que elija una opción y realiza la operación correspondiente.
# El programa continuará ejecutándose hasta que el usuario decida salir.
# Autor: [Gabriel Ochoa]
while True:
    print("Bienvenido al sistema de cajero automatico BANCO BNC")
    print("Por favor, elija una opcion:")                         
    print("Opcion 1= Retiro")   
    print("Opcion 2= Deposito")
    print("Opcion 3= Consulta")
    print("Opcion 4= Cambio de Clave")
    print("Opcion 5= Salir")
    op = int(input("Introduzca su opcion: "))
    
    if op == 1:
            cuenta=int(input("Introduzca el numero de cuenta: "))  
            monto=int(input("Introduzca monto a retirar:"))
            print(f"Realizando Retiro al numero de cuenta:{cuenta} por monto de {monto}$")
            if monto > 0:
                boton = input("¿Desea confirmar el retiro? (s/n): ")
                if boton.lower() == 'n':
                    print("Retiro cancelado.")
                    print("No se pudo realizar elretiro, intente de nuevo.")
                    print("------------------------------------------------")
                    continue
                elif boton.lower() =='s':
                    vrcuenta=int(input("Introduzca los dos ultimos digitos de su cuenta: "))
                if vrcuenta != cuenta % 100:
                    print("Los dos ultimos digitos de la cuenta no coinciden. Intente de nuevo.")
                    print("------------------------------------------------")
                    continue
                else:
                    print(f"Retiro realizado con exito por {monto}$ de la cuenta {cuenta}.")
            break

    elif op == 2:
            cuenta=int(input("Introduzca el numero de cuenta: ")) 
            monto=int(input("Introduzca monto a depositar:"))
            print(f"Realizando Deposito al numero de cuenta:{cuenta} por monto de {monto}$")
            if monto > 0:
                boton = input("¿Desea confirmar el deposito? (s/n): ")
                if boton.lower() == 'n':
                    print("Deposito cancelado.")
                    print("No se pudo realizar el deposito, intente de nuevo.")
                    print("------------------------------------------------")
                    continue
                elif boton.lower() =='s':
                      vrcuenta=int(input("Introduzca los dos ultimos digitos de la cuenta: "))
                if vrcuenta != cuenta % 100:
                    print("Los dos ultimos digitos de la cuenta no coinciden. Intente de nuevo.")
                    print("------------------------------------------------")
                    continue            
                else:
                   print("Deposito realizado con exito.")
                break

    elif op == 3:
            cuenta =int(input("Introduzca el numero de cuenta: "))
            saldo = 1000  # Ejemplo de saldo, puede ser obtenido de una base de datos
            if saldo > 0:
                boton = input(f"¿Desea Consultar el numero de cuenta:{cuenta}? (s/n):")
                if boton.lower() == 'n':
                    print("Consulta cancelada.")
                    print("No se pudo realizar la consulta, intente de nuevo.")
                    print("------------------------------------------------")
                    continue
                elif boton.lower() =='s':
                      vrcuenta=int(input("Introduzca los dos ultimos digitos de la cuenta: ")) 
                if vrcuenta != int (cuenta) %100:
                         print("Los dos ultimos digitos de la cuenta no coinciden. Intente de nuevo.")
                         print("------------------------------------------------")
                         continue
                else:
                     print(f"Saldo actual: {saldo}$")
                     print("Consulta realizada con exito.")
            break
    elif op == 4:
            cuenta = input("Introduzca el numero de cuenta: ")
            clave_actual =int(input("Introduzca la clave actual: "))
            nueva_clave = int( input("Introduzca la nueva clave: ")) 
            confirmacion_clave =int(input("Confirme la nueva clave: "))
            if nueva_clave != confirmacion_clave:
                print("Las claves no coinciden. Intente de nuevo.")
                print("------------------------------------------------")
                continue
            print(f"Clave actualizada para la cuenta {cuenta}.")# Aquí se podría agregar lógica para actualizar la clave en una base de datos o sistema6
            print(f"Clave Nueva: {confirmacion_clave}")
            print("Cambio de Clave realizado con exito.")
            break
    elif op == 5:
            print("Saliendo del sistema...")
            break
    else:
            
            print("Opcion no valida, intente de nuevo.")
            print("------------------------------------------------")
    