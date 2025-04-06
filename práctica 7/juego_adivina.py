import tkinter as tk
from tkinter import messagebox
import random

class Juego:
    def __init__(self, numero_de_vidas):
        self.numero_de_vidas = numero_de_vidas
        self.record = 0

    def reinicia_partida(self):
        self.numero_de_vidas = 3

    def actualiza_record(self):
        if self.numero_de_vidas > self.record:
            self.record = self.numero_de_vidas

    def quita_vida(self):
        self.numero_de_vidas -= 1
        return self.numero_de_vidas > 0

class JuegoAdivinaNumero(Juego):
    def __init__(self, numero_de_vidas, ventana):
        super().__init__(numero_de_vidas)
        self.numero_a_adivinar = None
        self.ventana = ventana

    def juega(self):
        self.reinicia_partida()
        self.numero_a_adivinar = random.randint(0, 10)
        self.mostrar_interfaz()

    def mostrar_interfaz(self):
        self.ventana.title("Juego Adivina el Número")
        self.entrada_usuario = tk.Entry(self.ventana)
        self.entrada_usuario.pack(pady=10)

        self.boton_adivinar = tk.Button(self.ventana, text="Adivinar", command=self.adivinar)
        self.boton_adivinar.pack(pady=10)

        self.mensaje = tk.Label(self.ventana, text="Adivina el número entre 0 y 10:", font=("Arial", 14))
        self.mensaje.pack(pady=10)

    def adivinar(self):
        try:
            numero_usuario = int(self.entrada_usuario.get())
            if numero_usuario == self.numero_a_adivinar:
                messagebox.showinfo("¡Acertaste!", "¡Acertaste! Has adivinado el número.")
                self.actualiza_record()
                self.ventana.quit()
            else:
                if not self.quita_vida():
                    messagebox.showinfo("Game Over", "Te has quedado sin vidas.")
                    self.ventana.quit()
                else:
                    mensaje_pista = "El número es mayor." if numero_usuario < self.numero_a_adivinar else "El número es menor."
                    self.mensaje.config(text=f"{mensaje_pista}\nTienes {self.numero_de_vidas} vidas restantes.")
        except ValueError:
            messagebox.showwarning("Entrada no válida", "Por favor, ingresa un número válido.")

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def __init__(self, numero_de_vidas, ventana):
        super().__init__(numero_de_vidas, ventana)

    def valida_numero(self, numero):
        if 0 <= numero <= 10 and numero % 2 == 0:
            return True
        else:
            messagebox.showwarning("Número no válido", "El número debe ser par y estar entre 0 y 10.")
            return False

    def juega(self):
        self.reinicia_partida()
        self.numero_a_adivinar = random.choice([x for x in range(0, 11, 2)]) 
        self.mostrar_interfaz()

    def adivinar(self):
        try:
            numero_usuario = int(self.entrada_usuario.get())
            if self.valida_numero(numero_usuario):
                if numero_usuario == self.numero_a_adivinar:
                    messagebox.showinfo("¡Acertaste!", "¡Acertaste! Has adivinado el número par.")
                    self.actualiza_record()
                    self.ventana.quit()
                else:
                    if not self.quita_vida():
                        messagebox.showinfo("Game Over", "Te has quedado sin vidas.")
                        self.ventana.quit()
                    else:
                        mensaje_pista = "El número es mayor." if numero_usuario < self.numero_a_adivinar else "El número es menor."
                        self.mensaje.config(text=f"{mensaje_pista}\nTienes {self.numero_de_vidas} vidas restantes.")
        except ValueError:
            messagebox.showwarning("Entrada no válida", "Por favor, ingresa un número válido.")

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def __init__(self, numero_de_vidas, ventana):
        super().__init__(numero_de_vidas, ventana)

    def valida_numero(self, numero):
        if 0 <= numero <= 10 and numero % 2 != 0:
            return True
        else:
            messagebox.showwarning("Número no válido", "El número debe ser impar y estar entre 0 y 10.")
            return False

    def juega(self):
        self.reinicia_partida()
        self.numero_a_adivinar = random.choice([x for x in range(1, 11, 2)]) 
        self.mostrar_interfaz()

    def adivinar(self):
        try:
            numero_usuario = int(self.entrada_usuario.get())
            if self.valida_numero(numero_usuario):
                if numero_usuario == self.numero_a_adivinar:
                    messagebox.showinfo("¡Acertaste!", "¡Acertaste! Has adivinado el número impar.")
                    self.actualiza_record()
                    self.ventana.quit()
                else:
                    if not self.quita_vida():
                        messagebox.showinfo("Game Over", "Te has quedado sin vidas.")
                        self.ventana.quit()
                    else:
                        mensaje_pista = "El número es mayor." if numero_usuario < self.numero_a_adivinar else "El número es menor."
                        self.mensaje.config(text=f"{mensaje_pista}\nTienes {self.numero_de_vidas} vidas restantes.")
        except ValueError:
            messagebox.showwarning("Entrada no válida", "Por favor, ingresa un número válido.")

def main():
    ventana = tk.Tk()

    juego1 = JuegoAdivinaNumero(3, ventana)
    juego2 = JuegoAdivinaPar(3, ventana)
    juego3 = JuegoAdivinaImpar(3, ventana)

    boton_juego1 = tk.Button(ventana, text="Jugar Adivina el Número", command=juego1.juega)
    boton_juego1.pack(pady=10)

    boton_juego2 = tk.Button(ventana, text="Jugar Adivina un Número Par", command=juego2.juega)
    boton_juego2.pack(pady=10)

    boton_juego3 = tk.Button(ventana, text="Jugar Adivina un Número Impar", command=juego3.juega)
    boton_juego3.pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    main()
