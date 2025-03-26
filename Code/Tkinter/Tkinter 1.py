import tkinter as tk

from DIA1.primer_proyecto import resultado


# ______________________________

# Codigo interno
def contar_vocales():
  vocales = ['a', 'e', 'i', 'o', 'u']
  cadena = text.get("1.0", "end").lower() # Recibir la entrada del entry y guardarla en una variable
  conteo = {vocal: cadena.count(vocal) for vocal in vocales}
  resultado = " "

  for vocal, cantidad in conteo.items():
    resultado += f"La vocal '{vocal}' aparece {cantidad} veces\n"
    resultado_label.config(text=f"Aqui esta tu letra \n {resultado}")  # El resultado


# Codigo utilizado para limpiar la salida principal y poder utilizar otra palabra.
def limpiar():
    text.delete(0, tk.END)  # Borra el texto en el Entry
    resultado_label.config(text="eliminado")  # Borra el texto en el Label


# ______________________________
# creamos la ventana principal
root = tk.Tk() # abrir ventana
root.title("Contador de vocales") # Nombre de la ventana
root.geometry("400x550") # escala de la ventana
root.configure(bg="lightblue") # Ajustes de la ventana

# Frame agrupar widgets
frame = tk.Frame(root)
frame.pack()

# Mensaje para el usuario
label = tk.Label(root, text='Hola, porfavor ingresa una palabra para continuar.')
label.pack(padx=20, pady=10)
label.configure(bg="lightblue")

# widget para el input
# Ingresar o mostrar texto multilinea
text = tk.Text(root, height=5, width=40)
text.pack() # pack vendria siendo como un empaquetado de la eiqueta

# Boton que llama a la funcion
button = tk.Button(root, text="Consultar palabra", command=contar_vocales)
button.pack(padx=20, pady=5)
# FUNCIONES PARA RESPONDER A LA INTERRACION DEL USUARIO.

# Crear un Label para mostrar el resultado
resultado_label = tk.Label(root, text="Resultado:")
resultado_label.pack(pady=10)
resultado_label.config(bg="royalblue", fg="yellow", font=("Arial", 12))
"""
los terminos bg y fg significan respectivamente foreground y background.
"""

# Limpiar intento y reiniciar
limpiar_button = tk.Button(root, text="Borrar", command=limpiar)
limpiar_button.pack(pady=10)

# extras:
# button = tk.Button(root, text="Texto largo", width=20, height=2)
# label = tk.Label(root, text="Texto", padx=20, pady=10)

tk.mainloop()  # Finalizar bucle

"""

entry texto en una sola linea (no admite height)
text texto en multilinea (si lo admite), este requiere un parametro extra de cuanto puede leer.

"""