import tkinter as tk
from tkinter import ttk, messagebox
import random

class BingoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Juego de Bingo")
        self.geometry("1000x800")
        self.configure(bg="#f0f0f0")

        self.rango_maximo = None
        self.numeros_generados = set()
        self.numero_botones = {}
        
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Estilos para los colores
        self.style.configure("Fosforescente.TButton", foreground="#ffffff", background="#39FF14", font=("Helvetica", 12, "bold"))
        self.style.map("Fosforescente.TButton", background=[("pressed", "#218F0D"), ("active", "#42FF29")])
        
        self.style.configure("NumeroGrande.TLabel", background="#39FF14", foreground="black", font=("Helvetica", 60, "bold"))
        
        self.style.configure("NoSeleccionado.TButton", background="#808080", foreground="#ffffff", font=("Helvetica", 16), padding=10)
        self.style.configure("Seleccionado.TButton", background="#FFA500", foreground="#ffffff", font=("Helvetica", 16, "bold"), relief="sunken")
        
        # Estilo para las letras del BINGO
        self.style.configure("Letra.TLabel", font=("Helvetica", 24, "bold"))

        self.crear_widgets_configuracion()

    def crear_widgets_configuracion(self):
        for widget in self.winfo_children():
            widget.destroy()

        config_frame = ttk.Frame(self, padding="20")
        config_frame.pack(expand=True)

        ttk.Label(config_frame, text="Configuración del Juego", font=("Helvetica", 16, "bold")).pack(pady=10)
        
        ttk.Label(config_frame, text="Cantidad de números:", font=("Helvetica", 12)).pack(pady=5)
        self.entrada_rango = ttk.Entry(config_frame, width=10, font=("Helvetica", 12))
        self.entrada_rango.pack(pady=5)
        
        ttk.Button(config_frame, text="Iniciar Juego", command=self.iniciar_juego, style="Fosforescente.TButton").pack(pady=10)

    def iniciar_juego(self):
        try:
            rango_str = self.entrada_rango.get()
            rango = int(rango_str)
            if rango <= 0:
                raise ValueError
            self.rango_maximo = rango
            
            for widget in self.winfo_children():
                widget.destroy()
            self.crear_widgets_juego()
        except ValueError:
            messagebox.showerror("Error de Entrada", "Por favor, ingrese un número entero positivo.")

    def crear_widgets_juego(self):
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(expand=True, fill=tk.BOTH)
        
        grid_frame = ttk.Frame(main_frame)
        
        control_frame = ttk.Frame(main_frame, padding="10")
        control_frame.pack(side=tk.RIGHT, fill=tk.Y)
        grid_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        letras = ["B", "I", "N", "G", "O"]
        for i, letra in enumerate(letras):
            ttk.Label(grid_frame, text=letra, style="Letra.TLabel").grid(row=0, column=i * 2, columnspan=2, padx=5, pady=(0,10))

        # El código ahora se adapta a la cantidad de columnas
        columnas = 10
        filas = (self.rango_maximo + columnas - 1) // columnas
        
        for i in range(1, self.rango_maximo + 1):
            columna = (i - 1) % columnas
            fila = 1 + (i - 1) // columnas
            
            boton = ttk.Button(grid_frame, text=str(i), width=4, style="NoSeleccionado.TButton")
            boton.grid(row=fila, column=columna, padx=2, pady=2)
            self.numero_botones[i] = boton

        frame_numero = ttk.Frame(control_frame, style="NumeroGrande.TLabel")
        frame_numero.pack(pady=10, ipady=10, ipadx=10, fill=tk.X)
        self.etiqueta_numero = ttk.Label(frame_numero, text="-", style="NumeroGrande.TLabel")
        self.etiqueta_numero.pack(pady=10, padx=20, expand=True)

        self.boton_generar = ttk.Button(control_frame, text="Generar Número", command=self.generar_numero, style="Fosforescente.TButton")
        self.boton_generar.pack(pady=10, ipadx=10, ipady=5)
        
        ttk.Label(control_frame, text="Números salidos:", font=("Helvetica", 12)).pack(pady=(10, 0))
        self.listbox_numeros = tk.Listbox(control_frame, height=15, width=15, font=("Helvetica", 10))
        self.listbox_numeros.pack(pady=5, expand=True, fill=tk.BOTH)

        scrollbar = ttk.Scrollbar(control_frame, orient="vertical", command=self.listbox_numeros.yview)
        self.listbox_numeros.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        ttk.Button(control_frame, text="Reiniciar", command=self.reiniciar_juego).pack(pady=10)

    def reiniciar_juego(self):
        self.numeros_generados.clear()
        self.numero_botones.clear()
        self.crear_widgets_configuracion()

    def generar_numero(self):
        if len(self.numeros_generados) >= self.rango_maximo:
            self.etiqueta_numero.config(text="¡Fin!")
            self.boton_generar.config(state=tk.DISABLED)
            return

        while True:
            nuevo_numero = random.randint(1, self.rango_maximo)
            if nuevo_numero not in self.numeros_generados:
                self.numeros_generados.add(nuevo_numero)
                self.etiqueta_numero.config(text=str(nuevo_numero))
                self.actualizar_tablero(nuevo_numero)
                break

    def actualizar_tablero(self, numero):
        boton = self.numero_botones.get(numero)
        if boton:
            boton.config(style="Seleccionado.TButton")
            
        self.listbox_numeros.insert(tk.END, numero)
        self.listbox_numeros.yview(tk.END)

if __name__ == "__main__":
    app = BingoApp()
    app.mainloop()