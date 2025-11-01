import tkinter as tk
import random
import time

class ColorPuzzleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Colores Locos")
        self.root.configure(bg="#111")

        self.colors = ["red", "blue", "green", "yellow", "purple", "orange"]
        self.pattern = []
        self.user_input = []
        self.score = [0, 0]
        self.current_player = 0
        self.num_players = 1

        self.setup_menu()

    def setup_menu(self):
        self.menu_frame = tk.Frame(self.root, bg="#111")
        self.menu_frame.pack(pady=50)

        tk.Label(self.menu_frame, text="¿Cuántos jugadores?", fg="white", bg="#111", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.menu_frame, text="1 Jugador", command=lambda: self.start_game(1), font=("Arial", 14), bg="#444", fg="white").pack(pady=5)
        tk.Button(self.menu_frame, text="2 Jugadores", command=lambda: self.start_game(2), font=("Arial", 14), bg="#444", fg="white").pack(pady=5)

    def start_game(self, players):
        self.num_players = players
        self.menu_frame.destroy()
        self.build_interface()
        self.new_round()

    def build_interface(self):
        self.game_frame = tk.Frame(self.root, bg="#111")
        self.game_frame.pack()

        self.pattern_label = tk.Label(self.game_frame, text="", fg="white", bg="#111", font=("Arial", 14))
        self.pattern_label.pack(pady=10)

        self.buttons_frame = tk.Frame(self.game_frame, bg="#111")
        self.buttons_frame.pack()

        self.color_buttons = []
        for color in self.colors:
            btn = tk.Button(self.buttons_frame, bg=color, width=10, height=2,
                            command=lambda c=color: self.select_color(c))
            btn.pack(side="left", padx=5, pady=5)
            self.color_buttons.append(btn)

        self.status_label = tk.Label(self.game_frame, text="", fg="white", bg="#111", font=("Arial", 14))
        self.status_label.pack(pady=10)

    def new_round(self):
        self.user_input = []
        self.pattern = random.sample(self.colors, 4)
        self.pattern_label.config(text="Memoriza: " + " - ".join(self.pattern))
        self.root.after(2000, self.hide_pattern)

    def hide_pattern(self):
        self.pattern_label.config(text="Repite el patrón")
        self.status_label.config(text=f"Turno de Jugador {self.current_player + 1}")

    def select_color(self, color):
        self.user_input.append(color)
        if len(self.user_input) == len(self.pattern):
            self.check_pattern()

    def check_pattern(self):
        if self.user_input == self.pattern:
            self.score[self.current_player] += 1
            self.status_label.config(text=f"✅ Correcto! Puntos: {self.score[self.current_player]}")
        else:
            self.status_label.config(text=f"❌ Incorrecto. Era: {' - '.join(self.pattern)}")

        self.current_player = (self.current_player + 1) % self.num_players
        self.root.after(2000, self.new_round)

if __name__ == "__main__":
    root = tk.Tk()
    game = ColorPuzzleGame(root)
    root.mainloop()