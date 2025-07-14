import tkinter as tk
from tkinter import simpledialog, messagebox

# --- SIMULACIÓN DE LA BASE DE DATOS EN MEMORIA ---
# Estructura: {numero_cuenta: {'saldo': valor, 'pin': valor_pin}}
cuentas = {
    123456:  {'saldo': 1500.00, 'pin': 1234},
    678910: {'saldo': 500.00, 'pin': 5678},
    112233: {'saldo': 2500.75, 'pin': 9012}
}

# --- Funciones de las operaciones del Cajero ---

# Función auxiliar para verificar cuenta y PIN
def verificar_acceso(cuenta):
    if cuenta not in cuentas:
        messagebox.showerror("Error de Acceso", "Número de cuenta no encontrado.")
        return None, None # Retorna None para indicar fallo

    pin_ingresado = simpledialog.askinteger("Verificación de PIN", "Introduzca su PIN:")
    if pin_ingresado is None:
        messagebox.showinfo("Cancelado", "Operación cancelada.")
        return None, None # Retorna None si el usuario cancela el PIN

    if cuentas[cuenta]['pin'] != pin_ingresado:
        messagebox.showerror("Error de Acceso", "PIN incorrecto.")
        return None, None # Retorna None para indicar fallo

    return cuentas[cuenta], pin_ingresado # Retorna los datos de la cuenta y el PIN ingresado si es correcto


def retiro(numero_boton):
    cuenta = simpledialog.askinteger("Retiro", "Introduzca el número de cuenta:")
    if cuenta is None:
        messagebox.showinfo("Cancelado", "Operación de retiro cancelada.")
        return

    datos_cuenta, _ = verificar_acceso(cuenta) # Usamos _ porque no necesitamos el pin_ingresado aquí
    if datos_cuenta is None: # Si la verificación falló
        return

    monto = simpledialog.askinteger("Retiro", "Introduzca monto a retirar:")
    if monto is None:
        messagebox.showinfo("Cancelado", "Operación de retiro cancelada.")
        return
    
    if monto <= 0:
        messagebox.showerror("Error", "El monto a retirar debe ser positivo.")
        return

    if datos_cuenta['saldo'] < monto:
        messagebox.showerror("Error de Saldo", "Saldo insuficiente en la cuenta.")
        return

    confirmar = messagebox.askyesno("Confirmar", f"¿Desea retirar {monto}$ de la cuenta {cuenta}?")
    if confirmar:
        # Aquí ya no necesitamos los últimos dígitos, el PIN ya verificó la identidad
        datos_cuenta['saldo'] -= monto # Actualiza el saldo en la "base de datos"
        messagebox.showinfo("Éxito", f"Retiro realizado con éxito por {monto}$ de la cuenta {cuenta}.\nNuevo saldo: {datos_cuenta['saldo']}$")
    else:
        messagebox.showinfo("Cancelado", "Retiro cancelado.")


def deposito(numero_boton):
    cuenta = simpledialog.askinteger("Depósito", "Introduzca el número de cuenta:")
    if cuenta is None:
        messagebox.showinfo("Cancelado", "Operación de depósito cancelada.")
        return

    datos_cuenta, _ = verificar_acceso(cuenta)
    if datos_cuenta is None:
        return

    monto = simpledialog.askinteger("Depósito", "Introduzca monto a depositar:")
    if monto is None:
        messagebox.showinfo("Cancelado", "Operación de depósito cancelada.")
        return
    
    if monto <= 0:
        messagebox.showerror("Error", "El monto a depositar debe ser positivo.")
        return

    confirmar = messagebox.askyesno("Confirmar", f"¿Desea depositar {monto}$ en la cuenta {cuenta}?")
    if confirmar:
        datos_cuenta['saldo'] += monto # Actualiza el saldo
        messagebox.showinfo("Éxito", f"Depósito realizado con éxito por {monto}$ en la cuenta {cuenta}.\nNuevo saldo: {datos_cuenta['saldo']}$")
    else:
        messagebox.showinfo("Cancelado", "Depósito cancelado.")


def consulta(numero_boton):
    cuenta = simpledialog.askinteger("Consulta", "Introduzca el número de cuenta:")
    if cuenta is None:
        messagebox.showinfo("Cancelado", "Operación de consulta cancelada.")
        return

    datos_cuenta, _ = verificar_acceso(cuenta)
    if datos_cuenta is None:
        return

    confirmar = messagebox.askyesno("Confirmar", f"¿Desea consultar la cuenta {cuenta}?")
    if confirmar:
        # Aquí mostramos el saldo real de la "base de datos"
        messagebox.showinfo("Saldo", f"Saldo actual de la cuenta {cuenta}: {datos_cuenta['saldo']}$")
    else:
        messagebox.showinfo("Cancelado", "Consulta cancelada.")


def cambio_clave(numero_boton):
    cuenta = simpledialog.askinteger("Cambio de Clave", "Introduzca el número de cuenta:")
    if cuenta is None:
        messagebox.showinfo("Cancelado", "Operación de cambio de clave cancelada.")
        return

    # Verificar cuenta y PIN actual
    datos_cuenta, pin_actual_ingresado = verificar_acceso(cuenta)
    if datos_cuenta is None:
        return # Falló la verificación de cuenta o PIN

    nueva_clave = simpledialog.askinteger("Cambio de Clave", "Introduzca la nueva clave (4 dígitos):")
    if nueva_clave is None:
        messagebox.showinfo("Cancelado", "Operación de cambio de clave cancelada.")
        return
    
    # Opcional: Añadir validación para el formato del PIN (ej. 4 dígitos)
    if not (1000 <= nueva_clave <= 9999):
        messagebox.showerror("Error", "La nueva clave debe ser un número de 4 dígitos.")
        return

    confirmacion_clave = simpledialog.askinteger("Cambio de Clave", "Confirme la nueva clave:")
    if confirmacion_clave is None:
        messagebox.showinfo("Cancelado", "Operación de cambio de clave cancelada.")
        return

    if nueva_clave != confirmacion_clave:
        messagebox.showerror("Error", "Las claves no coinciden.")
    else:
        datos_cuenta['pin'] = nueva_clave # Actualiza el PIN en la "base de datos"
        messagebox.showinfo("Éxito", f"Clave actualizada para la cuenta {cuenta}.")


def salir():
    root.destroy()

# --- Configuración de la Ventana Principal ---
root = tk.Tk()
root.title("Cajero Automático BANCO BNC")

tk.Label(root, text="Bienvenido al sistema de cajero automático BANCO BNC", font=("Arial", 14)).pack(pady=10)

# --- Creación de Botones usando lambda para pasar un número ---
tk.Button(root, text="Retiro", width=20, command=lambda: retiro(1)).pack(pady=5)
tk.Button(root, text="Depósito", width=20, command=lambda: deposito(2)).pack(pady=5)
tk.Button(root, text="Consulta", width=20, command=lambda: consulta(3)).pack(pady=5)
tk.Button(root, text="Cambio de Clave", width=20, command=lambda: cambio_clave(4)).pack(pady=5)
tk.Button(root, text="Salir", width=20, command=salir).pack(pady=5)

# --- Iniciar el Bucle Principal de la Aplicación ---
root.mainloop()