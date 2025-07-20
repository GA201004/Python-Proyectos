# 04-cajero-automatico-sencillo.py
# Este es un programa sencillo de cajero automático que permite realizar operaciones básicas como retiro, depósito,
# consulta de saldo y cambio de clave. El programa solicita al usuario que elija una opción y realiza la operación correspondiente.
# El programa continuará ejecutándose hasta que el usuario decida salir.
# Autor: [Gabriel Ochoa]
import json
import os
CARPETA_DATOS = "C:\\Users\\Andry Ochoa\\Documents\\Proyectos Programacion\\Python\\Proyectos\\Base de Datos"
ARCHIVO_NOMBRE = "cuentas_banco.json"
ARCHIVO_CUENTAS = os.path.join(CARPETA_DATOS, ARCHIVO_NOMBRE)

def cargar_cuentas ():
     
     try:
          with open (ARCHIVO_CUENTAS,"r") as f:
               return json.load(f)
     except FileNotFoundError:
          return {123456789: {"saldo": 1500, "pin": "1234"},
                  234567891: {"saldo": 2500, "pin": "2345"},
                  345678912: {"saldo": 3500, "pin": "3456"},
                  456789123: {"saldo": 4500, "pin": "4567"},
                  567891234: {"saldo": 6500, "pin": "5678"}}
     except json.JSONDecodeError:
          return {123456789: {"saldo": 1500, "pin": "1234"},
                  234567891: {"saldo": 2500, "pin": "2345"},
                  345678912: {"saldo": 3500, "pin": "3456"},
                  456789123: {"saldo": 4500, "pin": "4567"},
                  567891234: {"saldo": 6500, "pin": "5678"}}
def guarda_cuentas(): 
     with open(ARCHIVO_CUENTAS,"w") as f:
          # json.dump() escribe el diccionario en el archivo en formato JSON
          json.dump(cuentas,f,indent=4)# indent=4 hace que el archivo sea más legible  
cuentas=cargar_cuentas()# Cargar las cuentas al inicio del programa 
def verificar_acceso(cuenta_num):
    cuenta_str=str(cuenta_num)
    if cuenta_str not in cuentas:
        print ("Error de Acceso", "Número de cuenta no encontrado.")
        return None, None

    pin_ingresado= input("Verificación de PIN", "Introduzca su PIN:")
    if cuentas[cuenta_str]["pin"] != pin_ingresado:
        print("Error de Acceso", "PIN incorrecto.")
        return None, None
    return cuenta_str, cuentas[cuenta_str] # Retorna los datos de la cuenta y el PIN ingresado

#  

    
def retiro():
    op=1
    cuenta=input("Retiro","Introduzca el numero de cuenta: ")
    if op==1:
         if cuenta is None: 
             print("Operacion Fallida")
             return
    datos_cuenta=verificar_acceso(cuenta)
    if datos_cuenta is None:
         print("Operacion Fallida")
         return
    monto= input(f"Retiro","Introduzca monto a retirar:","$")
    if monto is None:
        print("Operacion Fallida")
        return
    if monto<=0:
        print("Error", "El monto a retirar debe ser positivo.")
        return
    if datos_cuenta["saldo"]<monto:
         print("Saldo insuficiente en la cuenta.")
         return
    confirmar= input("Confirmar", f"¿Desea retirar {monto}$ de la cuenta {cuenta}?")
    if confirmar:
         boton = input("¿Desea confirmar el retiro? (s/n): ")
         datos_cuenta['saldo'] -= monto
            
         if boton.lower() == 'n':
              print("Retiro cancelado.")
              print("No se pudo realizar el retiro, intente de nuevo.")
              print("------------------------------------------------")
              return
         elif boton.lower() =='s':
                    vrcuenta=int(input("Introduzca los dos ultimos digitos de su cuenta: "))
                    if vrcuenta != cuenta % 100:
                         print("Los dos ultimos digitos de la cuenta no coinciden. Intente de nuevo.")
                         print("------------------------------------------------")
                    else:
                         print ("Éxito", f"Retiro realizado con éxito por {monto}$ de la cuenta {cuenta}.\nNuevo saldo: {datos_cuenta['saldo']}$")

# while True:
    


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
        retiro()
    elif op == 2:
        cuenta = int(input("Introduzca el numero de cuenta: "))
        monto = int(input("Introduzca monto a depositar:"))
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
          cuenta = int(input("Introduzca el numero de cuenta: "))
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
    