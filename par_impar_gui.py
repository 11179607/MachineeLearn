import tkinter as tk
from tkinter import simpledialog, messagebox

# 🪟 Crear ventana raíz una sola vez
root = tk.Tk()
root.withdraw()

# 🎯 Pedir número entero con validación personalizada
def pedir_numero_entero():
    while True:
        entrada = simpledialog.askstring("Clasificador de número", "Ingresa un número entero:")
        if entrada is None:
            return None  # Usuario canceló
        if entrada.isdigit() or (entrada.startswith('-') and entrada[1:].isdigit()):
            return int(entrada)
        else:
            messagebox.showerror("Error", "Por favor ingresa un número entero válido.")

# 🧾 Mostrar resultado
def mostrar_resultado(numero, es_impar):
    color = "red" if es_impar else "green"
    mensaje = f"El número {numero} es {'IMPAR' if es_impar else 'PAR'}"

    resultado = tk.Toplevel(root)
    resultado.title("Resultado")
    resultado.configure(bg=color)

    etiqueta = tk.Label(resultado, text=mensaje, font=("Arial", 16), fg="white", bg=color, padx=20, pady=20)
    etiqueta.pack()

    resultado.after(3000, resultado.destroy)
    resultado.mainloop()

# 🚀 Ejecución
numero = pedir_numero_entero()
if numero is not None:
    es_impar = numero % 2 != 0
    mostrar_resultado(numero, es_impar)
else:
    messagebox.showinfo("Cancelado", "No se ingresó ningún número.")