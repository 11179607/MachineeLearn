import tkinter as tk
from tkinter import simpledialog, messagebox

# Lista de palabras individuales (no frases)
SPAM_KEYWORDS = {
    "gratis", "urgente", "clic", "riesgo", "dinero", "promoción",
    "hoy", "garantizado", "actúa", "última", "inversión", "confidencial",
    "actualización", "problema", "seguridad", "bono", "oferta"
}

def contiene_spam(texto):
    palabras = texto.lower().split()
    return any(palabra in SPAM_KEYWORDS for palabra in palabras)

def mostrar_resultado(es_spam):
    ventana = tk.Tk()
    ventana.withdraw()

    color = "red" if es_spam else "green"
    mensaje = "⚠️ Posible SPAM detectado" if es_spam else "✅ El mensaje parece seguro"

    resultado = tk.Toplevel()
    resultado.title("Resultado del análisis")
    resultado.configure(bg=color)

    etiqueta = tk.Label(resultado, text=mensaje, font=("Arial", 16), fg="white", bg=color, padx=20, pady=20)
    etiqueta.pack()

    resultado.after(3000, resultado.destroy)
    resultado.mainloop()

def main():
    root = tk.Tk()
    root.withdraw()

    mensaje = simpledialog.askstring("Análisis de correo", "Escribe el cuerpo del correo para analizar:")
    if mensaje:
        es_spam = contiene_spam(mensaje)
        mostrar_resultado(es_spam)
    else:
        messagebox.showerror("Error", "No se ingresó ningún mensaje.")

if __name__ == "__main__":
    main()