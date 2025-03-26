import tkinter as tk

# Crear ventana principal
root = tk.Tk()
root.title("Ventana")
root.geometry("400x300")
root.configure(bg="red")

# Etiqueta
label = tk.Label(root, text="Hola, Luis!")
label.pack()

# Boton
def saludar():
    print("hola")


button = tk.Button(root, text="presioname", command=saludar())
button.pack()

# Entrada de texto
entry = tk.Entry(root)
entry.pack()

# cuadro de texto
text = tk.Text(root, height=5, width=30)
label = tk.Label(root, text="Ingresa un mensaje")
label.pack()
text.pack()

# Diseño con Frames
frame = tk.Frame(root, bg="lightyellow")
frame.pack()
label = tk.Label(frame, text="Dentro de un Frame", bg="lightyellow")
label.pack()

# Diseño con Grid
label1 = tk.Label(root, text="Usuario:", bg="white")
label1.grid(row=0, column=0)
entry1 = tk.Entry(root, bg="lightgrey")
entry1.grid(row=0, column=1)

# Capturar eventos como clics del raton o teclas presioandas
def on_key(event):
    print(f"Tecla presionada: {event.char}")


root.bind("<Key>", on_key)
root.destroy()
tk.mainloop()