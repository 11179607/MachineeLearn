import tkinter as tk
from tkinter import messagebox
import random

class CarreraDeDadosEstiloArcade:
    def __init__(self, root):
        self.root = root
        self.root.title("🎲 Carrera de Dados🎲")
        self.root.geometry("500x450")
        self.root.configure(bg="#1e1e2f")
        self.jugador1 = ""
        self.jugador2 = ""
        self.puntos = [0, 0]
        self.turno = 0
        self.en_juego = False
        self.pausado = False
        self.vs_computadora = False

        self.fuente = ("Consolas", 14, "bold")
        self.crear_pantalla_modo()

    def crear_pantalla_modo(self):
        self.limpiar_pantalla()
        self.titulo("🎲 Carrera de Dados🎲")
        self.boton("1 jugador (vs computadora)", self.configurar_un_jugador)
        self.boton("2 jugadores", self.configurar_dos_jugadores)

    def configurar_un_jugador(self):
        self.vs_computadora = True
        self.limpiar_pantalla()
        self.titulo("👤 Ingresa tu nombre")
        self.entry1 = self.entrada()
        self.boton("Iniciar Juego", self.iniciar_juego_un_jugador)

    def configurar_dos_jugadores(self):
        self.vs_computadora = False
        self.limpiar_pantalla()
        self.titulo("👥 Nombres de Jugadores")
        tk.Label(self.root, text="Jugador 1", font=self.fuente, bg="#1e1e2f", fg="white").pack()
        self.entry1 = self.entrada()
        tk.Label(self.root, text="Jugador 2", font=self.fuente, bg="#1e1e2f", fg="white").pack()
        self.entry2 = self.entrada()
        self.boton("Iniciar Juego", self.iniciar_juego_dos_jugadores)

    def iniciar_juego_un_jugador(self):
        self.jugador1 = self.entry1.get()
        self.jugador2 = "Computadora"
        if not self.jugador1:
            messagebox.showwarning("Falta nombre", "Por favor ingresa tu nombre.")
            return
        self.iniciar_juego()

    def iniciar_juego_dos_jugadores(self):
        self.jugador1 = self.entry1.get()
        self.jugador2 = self.entry2.get()
        if not self.jugador1 or not self.jugador2:
            messagebox.showwarning("Faltan nombres", "Por favor ingresa ambos nombres.")
            return
        self.iniciar_juego()

    def iniciar_juego(self):
        self.puntos = [0, 0]
        self.turno = 0
        self.en_juego = True
        self.pausado = False
        self.crear_tablero()

    def crear_tablero(self):
        self.limpiar_pantalla()
        self.estado_label = self.etiqueta("Estado: En juego")
        self.turno_label = self.etiqueta(f"Turno de: {self.jugador1}")
        self.puntaje_label = self.etiqueta(self.obtener_puntajes())
        self.dado_label = tk.Label(self.root, text="🎲", font=("Arial", 60), bg="#1e1e2f", fg="white")
        self.dado_label.pack(pady=10)

        self.boton("🎯 Lanzar Dado", self.lanzar_dado)
        self.boton("⏸️ Pausar", self.pausar)
        self.boton("▶️ Reanudar", self.reanudar)
        self.boton("🔄 Reiniciar", self.reiniciar)
        self.boton("🚪 Salir", self.root.quit)

    def lanzar_dado(self):
        if not self.en_juego:
            messagebox.showinfo("Juego terminado", "Reinicia el juego para volver a jugar.")
            return
        if self.pausado:
            messagebox.showinfo("Juego pausado", "Reanuda el juego para continuar.")
            return
        self.animar_dado()

    def animar_dado(self):
        for _ in range(15):
            cara = random.randint(1, 6)
            self.dado_label.config(text=str(cara))
            self.root.update()
            self.root.after(50)

        resultado = cara
        jugador_actual = self.turno % 2
        self.puntos[jugador_actual] += resultado
        self.puntaje_label.config(text=self.obtener_puntajes())

        if self.puntos[jugador_actual] >= 30:
            ganador = self.jugador1 if jugador_actual == 0 else self.jugador2
            self.estado_label.config(text="Estado: Finalizado")
            messagebox.showinfo("🎉 ¡Ganador!", f"{ganador} ha ganado con {self.puntos[jugador_actual]} puntos!")
            self.en_juego = False
        else:
            self.turno += 1
            siguiente = self.jugador1 if self.turno % 2 == 0 else self.jugador2
            self.turno_label.config(text=f"Turno de: {siguiente}")
            if self.vs_computadora and siguiente == "Computadora":
                self.root.after(1000, self.lanzar_dado)

    def obtener_puntajes(self):
        return f"{self.jugador1}: {self.puntos[0]} puntos | {self.jugador2}: {self.puntos[1]} puntos"

    def pausar(self):
        if self.en_juego and not self.pausado:
            self.pausado = True
            self.estado_label.config(text="Estado: Pausado")

    def reanudar(self):
        if self.pausado:
            self.pausado = False
            self.estado_label.config(text="Estado: En juego")
            if self.vs_computadora and self.turno % 2 == 1:
                self.root.after(500, self.lanzar_dado)

    def reiniciar(self):
        self.jugador1 = ""
        self.jugador2 = ""
        self.puntos = [0, 0]
        self.turno = 0
        self.en_juego = False
        self.pausado = False
        self.vs_computadora = False
        self.crear_pantalla_modo()

    # 🎨 Elementos visuales reutilizables
    def limpiar_pantalla(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def titulo(self, texto):
        tk.Label(self.root, text=texto, font=("Consolas", 20, "bold"), bg="#1e1e2f", fg="#00ffff").pack(pady=20)

    def etiqueta(self, texto):
        lbl = tk.Label(self.root, text=texto, font=self.fuente, bg="#1e1e2f", fg="white")
        lbl.pack(pady=5)
        return lbl

    def boton(self, texto, comando):
        tk.Button(self.root, text=texto, font=self.fuente, bg="#00aaff", fg="white",
                  activebackground="#0077cc", activeforeground="white", command=comando).pack(pady=5)

    def entrada(self):
        entry = tk.Entry(self.root, font=self.fuente, justify="center")
        entry.pack(pady=5)
        return entry

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = CarreraDeDadosEstiloArcade(root)
    root.mainloop()