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
def guardar_cuentas(): 
     with open(ARCHIVO_CUENTAS,"w") as f:
          # json.dump() escribe el diccionario en el archivo en formato JSON
          json.dump(cuentas,f,indent=4)# indent=4 hace que el archivo sea más legible  
cuentas=cargar_cuentas()# Cargar las cuentas al inicio del programa 
def verificar_acceso(cuenta_num):
    cuenta_str=str(cuenta_num)
    if cuenta_str not in cuentas:
        print ("Error de Acceso", "Número de cuenta no encontrado.")
        return None,None
   
    pin_ingresado = input("Introduzca su PIN:")
    if  str(cuentas[cuenta_str]["pin"]) != pin_ingresado:
        print("Error de Acceso", "PIN incorrecto.")
        return None, None
    return cuenta_str, cuentas[cuenta_str] # Retorna los datos de la cuenta y el PIN ingresado 
def retiro():

    cuenta=input("Introduzca el numero de cuenta: ")
    if not cuenta: 
         print("Operación Fallida: Número de cuenta no proporcionado.")
         return
    cuenta_str_validada,datos_cuenta=verificar_acceso(cuenta)
    if datos_cuenta is None:
         print("Operación Fallida: Cuenta no encontrada o acceso denegado.")
         return None,None
    try:
        # Se pide el monto. Se convierte a float para permitir decimales.
        monto_str = input(f"Introduzca monto a retirar de la cuenta {cuenta_str_validada}: $")
        monto = float(monto_str)
    except ValueError:
        print("Operación Fallida: Monto no válido. Por favor, ingrese un número.")
        return
    except Exception as e:
        # Captura cualquier otro error en la entrada del monto
        print(f"Operación Fallida: Error al leer el monto. {e}")
        return
    if monto <= 0:
        print("Operación Fallida: El monto a retirar debe ser un número positivo.")
        return

    # --- NUEVA VALIDACIÓN: Saldo Suficiente ---
    if monto > datos_cuenta['saldo']:
        print("Operación Fallida: Saldo insuficiente.")
        print(f"Su saldo actual es: {datos_cuenta['saldo']}$")
        return
    confirmacion_usuario = input(f"¿Desea retirar {monto}$ de la cuenta {cuenta}? (s/n): ").lower()

    if confirmacion_usuario == 's':
        # 8. Solicitar los dos últimos dígitos para una segunda verificación
        try:
            # Se convierte 'cuenta' a int para poder usar el operador módulo
            ultimos_dos_digitos_cuenta = int(cuenta) % 100
            vrcuenta = int(input("Introduzca los dos últimos dígitos de su cuenta para confirmar: "))
        except ValueError:
            print("Verificación Fallida: Entrada no válida para los dígitos de la cuenta.")
            print("Retiro cancelado.")
            return

        if vrcuenta != ultimos_dos_digitos_cuenta:
            print("Los dos últimos dígitos de la cuenta no coinciden. Intente de nuevo.")
            print("------------------------------------------------")
            print("Retiro cancelado.")
            return
        else:
            # Si todo es correcto, se realiza el retiro
            datos_cuenta['saldo'] -= monto
            guardar_cuentas()
            print("------------------------------------------------")
            print(f"Éxito: Retiro realizado con éxito por {monto}$ de la cuenta {cuenta}.")
            print(f"Nuevo saldo: {datos_cuenta['saldo']}$")
            print("------------------------------------------------")
    elif confirmacion_usuario == 'n':
        print("Retiro cancelado por el usuario.")
        print("------------------------------------------------")
    else:
        print("Opción no válida. Retiro cancelado.")
        print("------------------------------------------------")
def deposito(): 
    cuenta=input("Introduzca el numero de cuenta: ")
    if not cuenta: 
         print("Operación Fallida: Número de cuenta no proporcionado.")
         return
    cuenta_str_validada,datos_cuenta=verificar_acceso(cuenta)
    if datos_cuenta is None:
         print("Operación Fallida: Cuenta no encontrada o acceso denegado.")
         return None,None
    try:
        # Se pide el monto. Se convierte a float para permitir decimales.
        monto_str = input(f"Introduzca monto a deposita de la cuenta {cuenta_str_validada}: $")
        monto = float(monto_str)
    except ValueError:
        print("Operación Fallida: Monto no válido. Por favor, ingrese un número.")
        return
    except Exception as e:
        # Captura cualquier otro error en la entrada del monto
        print(f"Operación Fallida: Error al leer el monto. {e}")
        return
    if monto <= 0:
        print("Operación Fallida: El monto a depositar debe ser un número positivo.")
        return 
    confirmacion_usuario = input(f"¿Desea depositar {monto}$ en la cuenta {cuenta} a la cuenta? (s/n): ").lower()

    if confirmacion_usuario == 's':
        # 8. Solicitar los dos últimos dígitos para una segunda verificación
        try:
            # Se convierte 'cuenta' a int para poder usar el operador módulo
            ultimos_dos_digitos_cuenta = int(cuenta) % 100
            vrcuenta = int(input("Introduzca los dos últimos dígitos de su cuenta para confirmar: "))
        except ValueError:
            print("Verificación Fallida: Entrada no válida para los dígitos de la cuenta.")
            print("Retiro cancelado.")
            return

        if vrcuenta != ultimos_dos_digitos_cuenta:
            print("Los dos últimos dígitos de la cuenta no coinciden. Intente de nuevo.")
            print("------------------------------------------------")
            print("Retiro cancelado.")
            return
        else:
            # Si todo es correcto, se realiza el retiro
            datos_cuenta['saldo'] += monto
            guardar_cuentas()
            print("------------------------------------------------")
            print(f"Éxito: Depósito realizado con éxito por {monto}$ en la cuenta {cuenta_str_validada}.")
            print(f"Nuevo saldo: {datos_cuenta['saldo']}$")
            print("------------------------------------------------")
    elif confirmacion_usuario == 'n':
        print("Retiro cancelado por el usuario.")
        print("------------------------------------------------")
    else:
        print("Opción no válida. Deposito cancelado.")
        print("------------------------------------------------")
def consulta():

    print("\n--- CONSULTA DE SALDO ---")
    cuenta_ingresada = input("Introduzca el número de cuenta: ")
    if not cuenta_ingresada:
        print("Operación Fallida: Número de cuenta no proporcionado.")
        return

    cuenta_str_validada, datos_cuenta = verificar_acceso(cuenta_ingresada)

    if datos_cuenta is None:
        print("Operación Fallida: Cuenta no encontrada o acceso denegado.")
        return

    print("------------------------------------------------")
    print(f"Cuenta: {cuenta_str_validada}")
    print(f"Saldo actual: {datos_cuenta['saldo']}$")
    print("------------------------------------------------")
def cambio_de_clave():
    print("\n--- CAMBIO DE CLAVE (PIN) ---")
    cuenta_ingresada = input("Introduzca el número de cuenta: ")
    if not cuenta_ingresada:
        print("Operación Fallida: Número de cuenta no proporcionado.")
        return

    # Primero verificamos el acceso con el PIN actual
    cuenta_str_validada, datos_cuenta = verificar_acceso(cuenta_ingresada)

    if datos_cuenta is None:
        print("Operación Fallida: Cuenta no encontrada o acceso denegado.")
        return

    # Si el acceso es correcto, pedimos el nuevo PIN
    nuevo_pin = input("Introduzca el nuevo PIN (4 dígitos numéricos): ")

    # Validaciones básicas para el nuevo PIN
    if not nuevo_pin.isdigit() or len(nuevo_pin) != 4:
        print("Operación Fallida: El nuevo PIN debe ser de 4 dígitos numéricos.")
        return

    confirmar_nuevo_pin = input("Confirme el nuevo PIN: ")
    if nuevo_pin != confirmar_nuevo_pin:
        print("Operación Fallida: Los PINs no coinciden. Intente de nuevo.")
        return

    # Actualizar el PIN en los datos de la cuenta
    datos_cuenta['pin'] = int(nuevo_pin) # Guardar como entero si tus PINs son numéricos

    # Guardar los cambios en el archivo JSON
    guardar_cuentas()

    print("------------------------------------------------")
    print(f"Éxito: La clave (PIN) de la cuenta {cuenta_str_validada} ha sido cambiada exitosamente.")
    print("------------------------------------------------")
def crear_cuenta():
    print("\n--- CREAR NUEVA CUENTA ---")
    nueva_cuenta_num = input("Introduzca el número de la nueva cuenta (solo números): ")

    if not nueva_cuenta_num.isdigit():
        print("Operación Fallida: El número de cuenta debe contener solo dígitos.")
        return

    # Verificar si la cuenta ya existe
    if nueva_cuenta_num in cuentas:
        print(f"Operación Fallida: La cuenta {nueva_cuenta_num} ya existe.")
        return

    nuevo_pin = input("Introduzca el PIN para la nueva cuenta (4 dígitos numéricos): ")
    if not nuevo_pin.isdigit() or len(nuevo_pin) != 4:
        print("Operación Fallida: El PIN debe ser de 4 dígitos numéricos.")
        return

    # Opcional: Pedir un saldo inicial o establecerlo en 0
    try:
        saldo_inicial_str = input("Introduzca el saldo inicial (ej: 0.00): ")
        saldo_inicial = float(saldo_inicial_str)
        if saldo_inicial < 0:
            print("Operación Fallida: El saldo inicial no puede ser negativo. Se establecerá en 0.")
            saldo_inicial = 0.0
    except ValueError:
        print("Monto de saldo inicial no válido. Se establecerá el saldo inicial en 0.")
        saldo_inicial = 0.0

    # Añadir la nueva cuenta al diccionario global 'cuentas'
    cuentas[nueva_cuenta_num] = {
        "saldo": saldo_inicial,
        "pin": int(nuevo_pin) # Guardar el PIN como entero
    }

    # Guardar los cambios en el archivo JSON
    guardar_cuentas()

    print("------------------------------------------------")
    print(f"Éxito: La cuenta {nueva_cuenta_num} ha sido creada con un saldo inicial de {saldo_inicial}$.")
    print("------------------------------------------------")
def eliminar_cuenta():
    print("\n--- ELIMINAR CUENTA ---")
    cuenta_a_eliminar = input("Introduzca el número de cuenta a eliminar: ")
    if not cuenta_a_eliminar:
        print("Operación Fallida: Número de cuenta no proporcionado.")
        return

    # Verificar el acceso a la cuenta antes de eliminarla
    cuenta_str_validada, datos_cuenta = verificar_acceso(cuenta_a_eliminar)

    if datos_cuenta is None:
        print("Operación Fallida: Cuenta no encontrada o acceso denegado.")
        return

    # Opcional: Validación si el saldo no es cero
    if datos_cuenta['saldo'] != 0:
        print(f"Advertencia: La cuenta {cuenta_str_validada} tiene un saldo de {datos_cuenta['saldo']}$.")
        confirmar_eliminar = input("¿Desea eliminarla de todas formas? (s/n): ").lower()
        if confirmar_eliminar != 's':
            print("Operación cancelada: La cuenta no fue eliminada.")
            return

    confirmacion_usuario = input(f"¿Está seguro que desea eliminar la cuenta {cuenta_str_validada}? Esta acción es irreversible (s/n): ").lower()

    if confirmacion_usuario == 's':
        # Eliminar la cuenta del diccionario global 'cuentas'
        del cuentas[cuenta_str_validada]

        # Guardar los cambios en el archivo JSON
        guardar_cuentas()

        print("------------------------------------------------")
        print(f"Éxito: La cuenta {cuenta_str_validada} ha sido eliminada permanentemente.")
        print("------------------------------------------------")
    else:
        print("Operación cancelada: La cuenta no fue eliminada.")

# while True:
    


while True:

    print("Bienvenido al sistema de cajero automatico BANCO BNC")
    print("Por favor, elija una opcion:")                         
    print("Opcion 1= Retiro")   
    print("Opcion 2= Deposito")
    print("Opcion 3= Consulta")
    print("Opcion 4= Cambio de Clave")
    print("Opcion 5= Crear Cuenta")
    print("Opcion 6= Eliminar Cuenta")
    print("Opcion 7= Salir")
    op = int(input("Introduzca su opcion: "))
    if op == 1:
        retiro()
        print("------------------------------------------------")
    elif op ==2:
       deposito ()
       print("------------------------------------------------")


    elif op == 3:
      consulta()
      print("------------------------------------------------")
   
    elif op == 4:
           cambio_de_clave()
           print("------------------------------------------------")
    elif op == 5:
            crear_cuenta()
            print("------------------------------------------------")
    elif op ==6:
        eliminar_cuenta()
        print("------------------------------------------------")
    elif op ==7:
        print("Saliendo del sistema...")
        break
            
    else:
            
            print("Opcion no valida, intente de nuevo.")
            print("------------------------------------------------")
    