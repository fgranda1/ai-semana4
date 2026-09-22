import math
import tkinter as tk
from tkinter import messagebox

# 1. ALGORITMO MINIMAX CON PODA ALFA-BETA
def minimax_alfa_beta(n_cerillas, alfa, beta, es_maximizador):
    if n_cerillas == 0:
        return -10 if es_maximizador else 10

    if es_maximizador:
        mejor_valor = -math.inf
        for k in range(1, min(3, n_cerillas) + 1):
            valor = -10 if n_cerillas - k == 0 else minimax_alfa_beta(n_cerillas - k, alfa, beta, False)
            mejor_valor = max(mejor_valor, valor)
            alfa = max(alfa, valor)
            if beta <= alfa: break # Poda Beta
        return mejor_valor
    else:
        mejor_valor = math.inf
        for k in range(1, min(3, n_cerillas) + 1):
            valor = 10 if n_cerillas - k == 0 else minimax_alfa_beta(n_cerillas - k, alfa, beta, True)
            mejor_valor = min(mejor_valor, valor)
            beta = min(beta, valor)
            if beta <= alfa: break # Poda Alfa
        return mejor_valor

def obtener_mejor_movimiento(n_cerillas):
    mejor_valor, mejor_k = -math.inf, 1
    for k in range(1, min(3, n_cerillas) + 1):
        valor = -10 if n_cerillas - k == 0 else minimax_alfa_beta(n_cerillas - k, -math.inf, math.inf, False)
        if valor > mejor_valor:
            mejor_valor, mejor_k = valor, k
    return mejor_k

# 2. INTERFAZ GRÁFICA INTERACTIVA CON TKINTER
class JuegoCerillasTkinter:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Juego de las Cerillas (Nim) - IA Minimax + Alfa-Beta")
        self.ventana.geometry("480x380")
        self.ventana.configure(bg="#1e1e2e")
        self.cerillas = 15

        tk.Label(ventana, text="🔥 Juego de las Cerillas (Nim)", font=("Helvetica", 16, "bold"), fg="#cba6f7", bg="#1e1e2e").pack(pady=10)
        tk.Label(ventana, text="Regla: Quita 1, 2 o 3 cerillas. ¡Quien tome la ÚLTIMA pierde!", font=("Helvetica", 10), fg="#a6adc8", bg="#1e1e2e").pack()

        self.lbl_vis = tk.Label(ventana, text="🔥 " * 15, font=("Helvetica", 16), fg="#f9e2af", bg="#1e1e2e")
        self.lbl_vis.pack(pady=10)
        self.lbl_cnt = tk.Label(ventana, text="Cerillas restantes: 15", font=("Helvetica", 12, "bold"), fg="#89b4fa", bg="#1e1e2e")
        self.lbl_cnt.pack(pady=5)

        frame = tk.Frame(ventana, bg="#1e1e2e")
        frame.pack(pady=10)
        self.btn1 = tk.Button(frame, text="Quitar 1", bg="#a6e3a1", width=8, command=lambda: self.jugar_humano(1))
        self.btn1.grid(row=0, column=0, padx=5)
        self.btn2 = tk.Button(frame, text="Quitar 2", bg="#a6e3a1", width=8, command=lambda: self.jugar_humano(2))
        self.btn2.grid(row=0, column=1, padx=5)
        self.btn3 = tk.Button(frame, text="Quitar 3", bg="#a6e3a1", width=8, command=lambda: self.jugar_humano(3))
        self.btn3.grid(row=0, column=2, padx=5)

        self.lbl_est = tk.Label(ventana, text="Tu turno.", font=("Helvetica", 10, "italic"), fg="#f5e0dc", bg="#1e1e2e")
        self.lbl_est.pack(pady=10)

    def actualizar(self):
        self.lbl_vis.config(text="🔥 " * self.cerillas)
        self.lbl_cnt.config(text=f"Cerillas restantes: {self.cerillas}")

    def jugar_humano(self, cantidad):
        if self.cerillas >= cantidad:
            self.cerillas -= cantidad
            self.actualizar()
            if self.cerillas == 0:
                messagebox.showinfo("Fin del Juego", "❌ Tomaste la última cerilla. ¡Has perdido frente a la IA!")
                self.cerillas = 15; self.actualizar()
            else:
                self.ventana.after(400, self.jugar_ia)

    def jugar_ia(self):
        mov = obtener_mejor_movimiento(self.cerillas)
        self.cerillas -= mov
        self.actualizar()
        if self.cerillas == 0:
            messagebox.showinfo("Fin del Juego", "🎉 ¡La IA tomó la última cerilla! ¡Has ganado!")
            self.cerillas = 15; self.actualizar()
        else:
            self.lbl_est.config(text=f"🤖 La IA quitó {mov} cerilla(s). Tu turno.")

if __name__ == "__main__":
    raiz = tk.Tk(); app = JuegoCerillasTkinter(raiz); raiz.mainloop()