import tkinter as tk
from tkinter import simpledialog, messagebox
import json 
import os # Importa el módulo 'os' para trabajar con rutas de archivos

# --- Nombre del archivo y la carpeta donde se guardarán/cargarán los datos ---
# Ruta absoluta: Cambia 'C:/MiAppBanco/Datos' por la ruta real en tu sistema
# En Windows, usar barras inclinadas normales (/) o dobles barras invertidas (\\)
# En macOS/Linux, la ruta sería algo como '/home/tu_usuario/Documentos/MiAppBanco/Datos'
CARPETA_DATOS = "C:\\Users\\Andry Ochoa\\Documents\\Proyectos Programacion\\Python\\Proyectos\\Base de Datos"
ARCHIVO_NOMBRE = "cuentas_banco1.json"
ARCHIVO_CUENTAS = os.path.join(CARPETA_DATOS, ARCHIVO_NOMBRE) # Combina la carpeta y el nombre del archivo


# --- SIMULACIÓN DE LA BASE DE DATOS EN MEMORIA ---
# Intentamos cargar los datos del archivo. Si no existe, usamos los datos por defecto.
def cargar_cuentas():
    try:
        with open(ARCHIVO_CUENTAS, 'r') as f:
            # json.load() lee el contenido del archivo y lo convierte en un diccionario Python
            return json.load(f)
    except FileNotFoundError:
        # Si el archivo no existe, retornamos los datos iniciales por defecto
        return {
            "1234567890": {'saldo': 1500.00, 'pin': 1234}, # Las claves de JSON deben ser strings
            "9876543210": {'saldo': 500.00, 'pin': 5678},
            "1122334455": {'saldo': 2500.75, 'pin': 9012}
        }
    except json.JSONDecodeError:
        # Maneja el caso en que el archivo existe pero está vacío o corrupto
        messagebox.showwarning("Error de Archivo", "El archivo de datos está corrupto o vacío. Se usarán datos por defecto.")
        return {
            "1234567890": {'saldo': 1500.00, 'pin': 1234},
            "9876543210": {'saldo': 500.00, 'pin': 5678},
            "1122334455": {'saldo': 2500.75, 'pin': 9012}
        }

def guardar_cuentas():
    with open(ARCHIVO_CUENTAS, 'w') as f:
        # json.dump() escribe el diccionario en el archivo en formato JSON
        json.dump(cuentas, f, indent=4) # indent=4 hace que el archivo sea más legible


# Cargar las cuentas al inicio del programa
cuentas = cargar_cuentas()


# --- Función auxiliar para verificar cuenta y PIN ---
def verificar_acceso(cuenta_num):
    cuenta_str = str(cuenta_num)
    
    if cuenta_str not in cuentas:
        messagebox.showerror("Error de Acceso", "Número de cuenta no encontrado.")
        return None, None

    pin_ingresado = simpledialog.askinteger("Verificación de PIN", "Introduzca su PIN:")
    if pin_ingresado is None:
        messagebox.showinfo("Cancelado", "Operación cancelada.")
        return None, None

    if cuentas[cuenta_str]['pin'] != pin_ingresado:
        messagebox.showerror("Error de Acceso", "PIN incorrecto.")
        return None, None

    return cuentas[cuenta_str], pin_ingresado


# --- Funciones de las operaciones del Cajero ---

def retiro(numero_boton):
    cuenta = simpledialog.askinteger("Retiro", "Introduzca el número de cuenta:")
    if cuenta is None: return

    datos_cuenta, _ = verificar_acceso(cuenta)
    if datos_cuenta is None: return

    monto = simpledialog.askinteger("Retiro", "Introduzca monto a retirar:")
    if monto is None: return
    
    if monto <= 0:
        messagebox.showerror("Error", "El monto a retirar debe ser positivo.")
        return

    if datos_cuenta['saldo'] < monto:
        messagebox.showerror("Error de Saldo", "Saldo insuficiente en la cuenta.")
        return

    confirmar = messagebox.askyesno("Confirmar", f"¿Desea retirar {monto}$ de la cuenta {cuenta}?")
    if confirmar:
        datos_cuenta['saldo'] -= monto
        messagebox.showinfo("Éxito", f"Retiro realizado con éxito por {monto}$ de la cuenta {cuenta}.\nNuevo saldo: {datos_cuenta['saldo']}$")
        guardar_cuentas()
    else:
        messagebox.showinfo("Cancelado", "Retiro cancelado.")


def deposito(numero_boton):
    cuenta = simpledialog.askinteger("Depósito", "Introduzca el número de cuenta:")
    if cuenta is None: return

    datos_cuenta, _ = verificar_acceso(cuenta)
    if datos_cuenta is None: return

    monto = simpledialog.askinteger("Depósito", "Introduzca monto a depositar:")
    if monto is None: return
    
    if monto <= 0:
        messagebox.showerror("Error", "El monto a depositar debe ser positivo.")
        return

    confirmar = messagebox.askyesno("Confirmar", f"¿Desea depositar {monto}$ en la cuenta {cuenta}?")
    if confirmar:
        datos_cuenta['saldo'] += monto
        messagebox.showinfo("Éxito", f"Depósito realizado con éxito por {monto}$ en la cuenta {cuenta}.\nNuevo saldo: {datos_cuenta['saldo']}$")
        guardar_cuentas()
    else:
        messagebox.showinfo("Cancelado", "Depósito cancelado.")


def consulta(numero_boton):
    cuenta = simpledialog.askinteger("Consulta", "Introduzca el número de cuenta:")
    if cuenta is None: return

    datos_cuenta, _ = verificar_acceso(cuenta)
    if datos_cuenta is None: return

    confirmar = messagebox.askyesno("Confirmar", f"¿Desea consultar la cuenta {cuenta}?")
    if confirmar:
        messagebox.showinfo("Saldo", f"Saldo actual de la cuenta {cuenta}: {datos_cuenta['saldo']}$")
    else:
        messagebox.showinfo("Cancelado", "Consulta cancelada.")


def cambio_clave(numero_boton):
    cuenta = simpledialog.askinteger("Cambio de Clave", "Introduzca el número de cuenta:")
    if cuenta is None: return

    datos_cuenta, _ = verificar_acceso(cuenta)
    if datos_cuenta is None: return

    nueva_clave = simpledialog.askinteger("Cambio de Clave", "Introduzca la nueva clave (4 dígitos):")
    if nueva_clave is None: return
    
    if not (1000 <= nueva_clave <= 9999): # Validación para PIN de 4 dígitos
        messagebox.showerror("Error", "La nueva clave debe ser un número de 4 dígitos.")
        return

    confirmacion_clave = simpledialog.askinteger("Cambio de Clave", "Confirme la nueva clave:")
    if confirmacion_clave is None: return

    if nueva_clave != confirmacion_clave:
        messagebox.showerror("Error", "Las claves no coinciden.")
    else:
        datos_cuenta['pin'] = nueva_clave
        messagebox.showinfo("Éxito", f"Clave actualizada para la cuenta {cuenta}.")
        guardar_cuentas()


### **Nuevas Funciones: Crear y Borrar Cuenta**


def crear_cuenta():
    while True: # Bucle para asegurar un número de cuenta válido y no existente
        nueva_cuenta = simpledialog.askinteger("Crear Cuenta", "Introduzca el nuevo número de cuenta (6 dígitos):")
        if nueva_cuenta is None:
            messagebox.showinfo("Cancelado", "Creación de cuenta cancelada.")
            return

        # Validación básica de 9 dígitos
        if not (100000 <= nueva_cuenta <= 999999):
            messagebox.showerror("Error", "El número de cuenta debe ser de 6 dígitos.")
            continue # Pide de nuevo el número de cuenta

        nueva_cuenta_str = str(nueva_cuenta)
        if nueva_cuenta_str in cuentas:
            messagebox.showerror("Error", "El número de cuenta ya existe. Por favor, elija otro.")
        else:
            break # El número de cuenta es válido y no existe, salir del bucle

    while True: # Bucle para asegurar un PIN válido y confirmado
        nuevo_pin = simpledialog.askinteger("Crear Cuenta", "Introduzca el PIN para la nueva cuenta (4 dígitos):")
        if nuevo_pin is None:
            messagebox.showinfo("Cancelado", "Creación de cuenta cancelada.")
            return
        
        if not (1000 <= nuevo_pin <= 9999):
            messagebox.showerror("Error", "El PIN debe ser un número de 4 dígitos.")
            continue

        confirmar_pin = simpledialog.askinteger("Crear Cuenta", "Confirme el PIN:")
        if confirmar_pin is None:
            messagebox.showinfo("Cancelado", "Creación de cuenta cancelada.")
            return

        if nuevo_pin != confirmar_pin:
            messagebox.showerror("Error", "Los PINs no coinciden. Inténtelo de nuevo.")
        else:
            break # PIN válido y confirmado, salir del bucle

    saldo_inicial = simpledialog.askfloat("Crear Cuenta", "Introduzca el saldo inicial:")
    if saldo_inicial is None:
        messagebox.showinfo("Cancelado", "Creación de cuenta cancelada.")
        return
    
    if saldo_inicial < 0:
        messagebox.showerror("Error", "El saldo inicial no puede ser negativo.")
        return

    confirmar = messagebox.askyesno("Confirmar Creación",
                                    f"¿Desea crear la cuenta {nueva_cuenta_str} con saldo {saldo_inicial}$ y PIN {nuevo_pin}?")
    if confirmar:
        cuentas[nueva_cuenta_str] = {'saldo': saldo_inicial, 'pin': nuevo_pin}
        guardar_cuentas()
        messagebox.showinfo("Éxito", f"Cuenta {nueva_cuenta_str} creada con éxito.")
    else:
        messagebox.showinfo("Cancelado", "Creación de cuenta cancelada.")


def borrar_cuenta():
    cuenta_a_borrar = simpledialog.askinteger("Borrar Cuenta", "Introduzca el número de cuenta a borrar:")
    if cuenta_a_borrar is None:
        messagebox.showinfo("Cancelado", "Borrado de cuenta cancelado.")
        return

    cuenta_a_borrar_str = str(cuenta_a_borrar)

    if cuenta_a_borrar_str not in cuentas:
        messagebox.showerror("Error", "El número de cuenta no existe.")
        return

    # Solicitar PIN para confirmar borrado
    pin_ingresado = simpledialog.askinteger("Borrar Cuenta", "Introduzca el PIN de la cuenta para confirmar:")
    if pin_ingresado is None:
        messagebox.showinfo("Cancelado", "Borrado de cuenta cancelado.")
        return

    if cuentas[cuenta_a_borrar_str]['pin'] != pin_ingresado:
        messagebox.showerror("Error", "PIN incorrecto. No se puede borrar la cuenta.")
        return

    confirmar = messagebox.askyesno("Confirmar Borrado",
                                    f"¿Está seguro que desea borrar la cuenta {cuenta_a_borrar_str}? ¡Esta acción es irreversible!")
    if confirmar:
        del cuentas[cuenta_a_borrar_str] # Elimina la cuenta del diccionario
        guardar_cuentas()
        messagebox.showinfo("Éxito", f"Cuenta {cuenta_a_borrar_str} borrada con éxito.")
    else:
        messagebox.showinfo("Cancelado", "Borrado de cuenta cancelado.")


def salir():
    guardar_cuentas()
    root.destroy()

# --- Configuración de la Ventana Principal ---
root = tk.Tk()
root.title("Cajero Automático BANCO BNC")

tk.Label(root, text="Bienvenido al sistema de cajero automático BANCO BNC", font=("Arial", 14)).pack(pady=10)

# --- Creación de Botones ---
tk.Button(root, text="Retiro", width=20, command=lambda: retiro(1)).pack(pady=5)
tk.Button(root, text="Depósito", width=20, command=lambda: deposito(2)).pack(pady=5)
tk.Button(root, text="Consulta", width=20, command=lambda: consulta(3)).pack(pady=5)
tk.Button(root, text="Cambio de Clave", width=20, command=lambda: cambio_clave(4)).pack(pady=5)
tk.Button(root, text="Crear Cuenta", width=20, command=crear_cuenta).pack(pady=5) # Nuevo botón
tk.Button(root, text="Borrar Cuenta", width=20, command=borrar_cuenta).pack(pady=5) # Nuevo botón
tk.Button(root, text="Salir", width=20, command=salir).pack(pady=5)

# --- Iniciar el Bucle Principal de la Aplicación ---
root.mainloop()