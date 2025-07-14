import tkinter as tk
from tkinter import simpledialog, messagebox
import json # Importa el módulo json
import os # Importa el módulo 'os' para trabajar con rutas de archivos

# --- Nombre del archivo y la carpeta donde se guardarán/cargarán los datos ---
# Ruta absoluta: Cambia 'C:/MiAppBanco/Datos' por la ruta real en tu sistema
# En Windows, usar barras inclinadas normales (/) o dobles barras invertidas (\\)
# En macOS/Linux, la ruta sería algo como '/home/tu_usuario/Documentos/MiAppBanco/Datos'
CARPETA_DATOS = "C:\\Users\\Andry Ochoa\\Documents\\Proyectos Programacion\\Python\\Proyectos\\Base de Datos"
ARCHIVO_NOMBRE = "cuentas_banco.json"
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
        return { # Las claves de JSON deben ser strings
            123456:  {'saldo': 1500.00, 'pin': 1234},
            678910: {'saldo': 500.00, 'pin': 5678},
            112233: {'saldo': 2500.75, 'pin': 9012}
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


# --- Función auxiliar para verificar cuenta y PIN (sin cambios significativos) ---
def verificar_acceso(cuenta_num): # Renombrado a cuenta_num para evitar conflicto con la variable 'cuenta' global
    # Las claves en JSON son strings, así que convertimos el número de cuenta a string para buscarla
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

    return cuentas[cuenta_str], pin_ingresado # Retorna los datos de la cuenta y el PIN ingresado


# --- Funciones de las operaciones del Cajero (actualizadas para usar string como clave de cuenta) ---

def retiro(numero_boton):
    cuenta = simpledialog.askinteger("Retiro", "Introduzca el número de cuenta:")
    if cuenta is None: return

    # Pasamos el número de cuenta directamente a verificar_acceso, que lo convierte a string
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
        guardar_cuentas() # ¡Guardar después de cada modificación!
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
        guardar_cuentas() # ¡Guardar después de cada modificación!
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
    
    if not (1000 <= nueva_clave <= 9999):
        messagebox.showerror("Error", "La nueva clave debe ser un número de 4 dígitos.")
        return

    confirmacion_clave = simpledialog.askinteger("Cambio de Clave", "Confirme la nueva clave:")
    if confirmacion_clave is None: return

    if nueva_clave != confirmacion_clave:
        messagebox.showerror("Error", "Las claves no coinciden.")
    else:
        datos_cuenta['pin'] = nueva_clave
        messagebox.showinfo("Éxito", f"Clave actualizada para la cuenta {cuenta}.")
        guardar_cuentas() # ¡Guardar después de cada modificación!


def salir():
    # Aunque guardamos en cada operación, una última guarda al salir asegura consistencia
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
tk.Button(root, text="Salir", width=20, command=salir).pack(pady=5)

# --- Iniciar el Bucle Principal de la Aplicación ---
root.mainloop()