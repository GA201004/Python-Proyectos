import tkinter as tk
from tkinter import simpledialog, messagebox

def retiro ():
    cuenta = simpledialog.askinteger("Retiro", "Introduzca el número de cuenta:")
    monto = simpledialog.askinteger("Retiro", "Introduzca monto a retirar:")
    if monto and monto > 0:
        confirmar = messagebox.askyesno("Confirmar", f"¿Desea retirar {monto}$ de la cuenta {cuenta}?")
        if confirmar:
            vrcuenta = simpledialog.askinteger("Verificación", "Introduzca los dos últimos dígitos de su cuenta:")
            if vrcuenta != cuenta % 100:
                messagebox.showerror("Error", "Los dos últimos dígitos no coinciden.")
            else:
                messagebox.showinfo("Éxito", f"Retiro realizado con éxito por {monto}$ de la cuenta {cuenta}.")
        else:
            messagebox.showinfo("Cancelado", "Retiro cancelado.")

def deposito():
    cuenta = simpledialog.askinteger("Depósito", "Introduzca el número de cuenta:")
    monto = simpledialog.askinteger("Depósito", "Introduzca monto a depositar:")
    if monto and monto > 0:
        confirmar = messagebox.askyesno("Confirmar", f"¿Desea depositar {monto}$ en la cuenta {cuenta}?")
        if confirmar:
            vrcuenta = simpledialog.askinteger("Verificación", "Introduzca los dos últimos dígitos de la cuenta:")
            if vrcuenta != cuenta % 100:
                messagebox.showerror("Error", "Los dos últimos dígitos no coinciden.")
            else:
                messagebox.showinfo("Éxito", "Depósito realizado con éxito.")
        else:
            messagebox.showinfo("Cancelado", "Depósito cancelado.")

def consulta():
    cuenta = simpledialog.askinteger("Consulta", "Introduzca el número de cuenta:")
    saldo = 1000  # Ejemplo, aquí deberías consultar la base de datos
    confirmar = messagebox.askyesno("Confirmar", f"¿Desea consultar la cuenta {cuenta}?")
    if confirmar:
        vrcuenta = simpledialog.askinteger("Verificación", "Introduzca los dos últimos dígitos de la cuenta:")
        if vrcuenta != cuenta % 100:
            messagebox.showerror("Error", "Los dos últimos dígitos no coinciden.")
        else:
            messagebox.showinfo("Saldo", f"Saldo actual: {saldo}$")
    else:
        messagebox.showinfo("Cancelado", "Consulta cancelada.")

def cambio_clave():
    cuenta = simpledialog.askinteger("Cambio de Clave", "Introduzca el número de cuenta:")
    clave_actual = simpledialog.askinteger("Cambio de Clave", "Introduzca la clave actual:")
    nueva_clave = simpledialog.askinteger("Cambio de Clave", "Introduzca la nueva clave:")
    confirmacion_clave = simpledialog.askinteger("Cambio de Clave", "Confirme la nueva clave:")
    if nueva_clave != confirmacion_clave:
        messagebox.showerror("Error", "Las claves no coinciden.")
    else:
        messagebox.showinfo("Éxito", f"Clave actualizada para la cuenta {cuenta}.")

def salir():
    root.destroy()

root = tk.Tk()
root.title("Cajero Automático BANCO BNC")

tk.Label(root, text="Bienvenido al sistema de cajero automático BANCO BNC", font=("Arial", 14)).pack(pady=10)
tk.Button(root, text="Retiro", width=20, command=retiro).pack(pady=5)
tk.Button(root, text="Depósito", width=20, command=deposito).pack(pady=5)
tk.Button(root, text="Consulta", width=20, command=consulta).pack(pady=5)
tk.Button(root, text="Cambio de Clave", width=20, command=cambio_clave).pack(pady=5)
tk.Button(root, text="Salir", width=20, command=salir).pack(pady=5)
root.mainloop()