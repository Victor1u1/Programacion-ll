import tkinter as tk
from PIL import Image, ImageTk

class Boleto:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.precio = 0.0

    def mostrar(self):
        return f"Cantidad: {self.cantidad}, Precio Total: {self.precio:.1f}"

class Palco(Boleto):
    def __init__(self, cantidad):
        super().__init__(cantidad)
        self.precio = 100.0 * cantidad

class Platea(Boleto):
    def __init__(self, cantidad, dias):
        super().__init__(cantidad)
        precio_unitario = 50.0 if dias >= 10 else 60.0
        self.precio = precio_unitario * cantidad

class Galeria(Boleto):
    def __init__(self, cantidad, dias):
        super().__init__(cantidad)
        precio_unitario = 25.0 if dias >= 10 else 30.0
        self.precio = precio_unitario * cantidad

def vender():
    tipo_boleto = tipo.get()
    try:
        cantidad = int(entry_cantidad.get())
        dias = int(entry_dias.get()) if tipo_boleto != "Palco" else 0

        if cantidad <= 0:
            resultado.config(text="La cantidad debe ser mayor que 0.")
            return

        if tipo_boleto == "Palco":
            boleto = Palco(cantidad)
        elif tipo_boleto == "Platea":
            boleto = Platea(cantidad, dias)
        elif tipo_boleto == "Galeria":
            boleto = Galeria(cantidad, dias)
        else:
            resultado.config(text="Seleccione un tipo de boleto.")
            return

        resultado.config(text=f"Tipo: {tipo_boleto}\nCantidad: {boleto.cantidad}\nPrecio Total: {boleto.precio:.1f}")
    except ValueError:
        resultado.config(text="Datos inválidos. Ingrese números válidos.")

ventana = tk.Tk()
ventana.title("Teatro Municipal")
ventana.geometry("450x400")
ventana.resizable(False, False)

frame_superior = tk.LabelFrame(ventana, text="", padx=10, pady=10)
frame_superior.pack(padx=10, pady=5, fill="x")

tk.Label(frame_superior, text="Teatro Municipal", font=("Arial", 16, "bold")).pack(side="left")

try:
    img = Image.open("teatro.jpg")  
    img = img.resize((100, 70))
    foto = ImageTk.PhotoImage(img)
    lbl_img = tk.Label(frame_superior, image=foto)
    lbl_img.image = foto
    lbl_img.pack(side="right")
except:
    tk.Label(frame_superior, text="[Sin imagen]").pack(side="right")

frame_datos = tk.LabelFrame(ventana, text="Datos del Boleto", padx=10, pady=10)
frame_datos.pack(padx=10, pady=5, fill="x")

tipo = tk.StringVar(value="Ninguno")
tk.Radiobutton(frame_datos, text="Palco", variable=tipo, value="Palco").grid(row=0, column=0, sticky='w')
tk.Radiobutton(frame_datos, text="Platea", variable=tipo, value="Platea").grid(row=0, column=1, sticky='w')
tk.Radiobutton(frame_datos, text="Galeria", variable=tipo, value="Galeria").grid(row=0, column=2, sticky='w')

tk.Label(frame_datos, text="Cantidad de Boletos:").grid(row=1, column=0, pady=5, sticky='e')
entry_cantidad = tk.Entry(frame_datos, width=10)
entry_cantidad.grid(row=1, column=1, pady=5, sticky='w')

tk.Label(frame_datos, text="Cant. Días para el Evento:").grid(row=2, column=0, columnspan=2, pady=5, sticky='e')
entry_dias = tk.Entry(frame_datos, width=10)
entry_dias.grid(row=2, column=2, pady=5, sticky='w')

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)
tk.Button(frame_botones, text="Vende", width=10, command=vender).grid(row=0, column=0, padx=10)
tk.Button(frame_botones, text="Salir", width=10, command=ventana.destroy).grid(row=0, column=1, padx=10)

frame_info = tk.LabelFrame(ventana, text="Información", padx=10, pady=10)
frame_info.pack(padx=10, pady=5, fill="x")

resultado = tk.Label(frame_info, text="", font=("Arial", 12), fg="blue")
resultado.pack()

ventana.mainloop()
