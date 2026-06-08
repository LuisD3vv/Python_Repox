from tkinter import *
import random
import datetime
from tkinter import filedialog,messagebox

operador = ''

precios_comida:float = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05]
precios_bebida:float = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00]
precios_postres:float = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94]


def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END,operador)

def borrar():
    global operador
    operador = ""
    visor_calculadora.delete(0,END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(0,resultado)
    operador = ""

def revisar_check():
    # Checkbuttons para comidas
    x = 0
    for c in cuadros_comidas:
        if variables_comidas[x].get() == 1:
            cuadros_comidas[x].config(state=NORMAL)
            if cuadros_comidas[x].get() == '0':
                cuadros_comidas[x].delete(0,END)
            cuadros_comidas[x].focus()
        else:
            cuadros_comidas[x].config(state=DISABLED)
            texto_comidas[x].set('0')
        x += 1

    # Checkbuttons para bebidas
    x = 0
    for b in cuadros_bebidas:
        if variables_bebidas[x].get() == 1:
            cuadros_bebidas[x].config(state=NORMAL)
            if cuadros_bebidas[x].get() == '0':
                cuadros_bebidas[x].delete(0,END)
            cuadros_bebidas[x].focus()
        else:
            cuadros_bebidas[x].config(state=DISABLED)
            texto_bebidas[x].set('0')
        x += 1
    # Checkbuttons para postres
    x = 0
    for p in cuadros_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0,END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1

def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comidas:    
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1
    
    
    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebidas:    
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1
    
    
    sub_total_postres = 0
    p = 0
    for cantidad in texto_postres:    
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[p])
        p += 1
    
    sub_total = sub_total_comida + sub_total_bebida + sub_total_postres
    impuestos = sub_total * 0.07
    total = sub_total + impuestos
    
    var_costo_comidas.set(f'$ {round(sub_total_comida,2)}')
    var_costo_bebidas.set(f'$ {round(sub_total_bebida,2)}')
    var_costo_postres.set(f'$ {round(sub_total_postres,2)}')
    var_subtotal.set(f'${round(sub_total,2)}')
    var_impuesto.set(f'$ {round(impuestos,2)}')
    var_total.set(f'$ {round(total,2)}')

def recibo():
    texto_recibo.delete(1.0,END)
    num_recibo = f'N# - {random.randint(1000,9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}' # tambien se puede con strptime
    texto_recibo.insert(END,f'Datos:\t{num_recibo}\t{fecha_recibo}\n')
    texto_recibo.insert(END,f"*"*30+ '\n')
    texto_recibo.insert(END,'Items\tCant.\tCosto Items\n')
    texto_recibo.insert(END,f"-"*45 + '\n')
    
    x = 0
    for comida in texto_comidas:
        if comida.get() != '0':
            texto_recibo.insert(END,f'{lista_comidas[x]}\t{comida.get()}\t${float(comida.get())*precios_comida[x]}\n')
        x+=1
    x = 0
    for bebida in texto_bebidas:
        if bebida.get() != '0':
            texto_recibo.insert(END,f'{lista_bebidas[x]}\t{bebida.get()}\t${float(bebida.get())*precios_bebida[x]}\n')
        x+=1
    x = 0
    for postre in texto_postres:
        if postre.get() != '0':
            texto_recibo.insert(END,f'{lista_postres[x]}\t{postre.get()}\t${float(postre.get())*precios_postres[x]}\n')
        x+=1
        
    texto_recibo.insert(END,f"-"*45 + '\n')
    texto_recibo.insert(END,f'Costo de la comida: \t\t{var_costo_comidas.get()}\n')
    texto_recibo.insert(END,f'Costo de la bebida: \t\t{var_costo_bebidas.get()}\n')
    texto_recibo.insert(END,f'Costo de la postres: \t\t{var_costo_postres.get()}\n')
    texto_recibo.insert(END,f"-"*45 + '\n')
    texto_recibo.insert(END,f'Subtotal: \t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END,f'impuestos: \t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END,f'Total: \t\t{var_total.get()}\n')
    texto_recibo.insert(END,f"*"*30+ '\n')
    texto_recibo.insert(END,'Lo esperamos pronto.')

def guardar():
    info_recibo = texto_recibo.get(1.0,END)
    archivo = filedialog.asksaveasfile(mode="w",defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo("Informacion","Su recibo se ha generado.")

def resetear():
    texto_recibo.delete(0.1,END)
    
    for texto in texto_comidas:
        texto.set('0')
    for bebidas in texto_bebidas:
        bebidas.set('0')
    for postres in texto_postres:
        postres.set('0')
        
    for cuadro in cuadros_comidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)
    
    for v in variables_comidas:
        v.set('0')
    for v in variables_bebidas:
        v.set('0')
    for v in variables_postres:
        v.set('0')
        
    var_costo_comidas.set('')
    var_costo_bebidas.set('')
    var_costo_postres.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')
    
    messagebox.showinfo("Informacion","Se ha eliminado el contenido.")
# inciarlo
aplicacion = Tk()

# Tamano de la ventana, ancho,alto y cordenas x e y
aplicacion.geometry('1240x650+0+0')

#Evitar que se maximice
aplicacion.resizable(0,0)

# Titulo de la ventana
aplicacion.title('Sistema de Facturacion')

#color de fondo
aplicacion.config(bg='#222')


# panel superior
panel_superior = Frame(aplicacion,bd=1,relief=FLAT)
'''
geometria pack, cuenta con 3 diferentes maneras o enfoques con el cual podemos organizar
el contenido, esta el side, fill y expand

expand - si es verdadero llenara el espacio disponible del frame o ventana

fill -  determina si el widget va a llenar x o y espacio (vertical u horizontal) tiene 3 opciones, x,y y both (rellenar ambos)

side - para este tenemos cuatro constantes TOP,BOTTOM,LEFT, RIGHT

propagate - width y height.

Al usar el metodo side, actua sobre uno de los hijos
esto hace que el width y el height del frame padre original
dejen de tener efecto sobre el widget.

para conseguir que no se pierdan, debemos de indicarle a la fuincion del frame
de nuevo su width y height y efectuarlo con un pack propagate. con .config(width=200,height=260)

'''
panel_superior.pack(side=TOP)


# etiqueta titulo
etiqueta_titulo = Label(panel_superior,
                        text="Sistema de Facturación",
                        fg="azure4",
                        font=("Dosis",58),
                        bg="#222",
                        width=30)
etiqueta_titulo.grid(row=0,column=0)


# Panel izquierdo
panel_izquierdo = Frame(aplicacion,border=1,relief=FLAT)
panel_izquierdo.pack(side=LEFT,expand=True,fill=BOTH)

# Panel costos
panel_costos = Frame(panel_izquierdo,bd=1,relief=FLAT,bg="azure4",padx=90)
panel_costos.pack(side=BOTTOM)

#Panel comidas
panel_comidas = LabelFrame(panel_izquierdo,text="Comidas",font=("Dosis",15,'bold'),
                            bd=1,relief=FLAT,fg="azure4")
panel_comidas.pack(side=LEFT)

#Panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo,text="Bebidas",font=("Dosis",15,'bold'),
                            bd=1,relief=FLAT,fg="azure4")
panel_bebidas.pack(side=LEFT)


#Panel postres
panel_postres = LabelFrame(panel_izquierdo,text="Postres",font=("Dosis",15,'bold'),
                            bd=1,relief=FLAT,fg="azure4")
panel_postres.pack(side=LEFT)

# Panel derecha
panel_derecha = Frame(aplicacion,bd=1,relief=FLAT)
panel_derecha.pack(side=RIGHT)

# panel calculadora
panel_calculadora = Frame(panel_derecha,bd=1,relief=FLAT,bg="#222")
panel_calculadora.pack(expand=True,fill=BOTH)


# panel recibo
panel_recibo = Frame(panel_derecha,bd=1,relief=FLAT,bg="#222")
panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_derecha,bd=1,relief=FLAT,bg="#222")
panel_botones.pack()

#listas de productos
lista_comidas = ["pollo","salmon","pizza","camaron","ribeye","pozole","menudo"]
lista_bebidas = ["agua","soda","jugo","cafe","wiskey","ron","tequila"]
lista_postres = ["pastel","helado",'fruta',"brownie","flan","yogurt","dulces"]

# generar items comidas
contador = 0
variables_comidas = []
cuadros_comidas = []
texto_comidas = []
for comidas in lista_comidas:
    # crear checkbuttons
    variables_comidas.append('')

    variables_comidas[contador] = IntVar()
    comidas = Checkbutton(panel_comidas,
                        text=comidas.title(),
                        font=("Dosis",18,'bold'),
                        onvalue=1,
                        offvalue=0,
                        variable=variables_comidas[contador],
                        command=revisar_check)
    comidas.grid(row=contador,column=0,sticky=W)
    # crear cuadros de entrada
    
    cuadros_comidas.append('')
    texto_comidas.append('')
    texto_comidas[contador] = StringVar()
    texto_comidas[contador].set(0)
    cuadros_comidas[contador] = Entry(panel_comidas,
                                font=('Dosis',18,'bold'),
                                bd=1,
                                width=6,
                                state=DISABLED,
                                textvariable=texto_comidas[contador])
    cuadros_comidas[contador].grid(row=contador,
                                column=1)
    contador += 1
    

# generar items bebidas
contador = 0
variables_bebidas = []
cuadros_bebidas = []
texto_bebidas = []
for bebidas in lista_bebidas:
    # crear checkbuttons
    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()
    bebidas = Checkbutton(panel_bebidas,
                        text=bebidas.title(),
                        font=("Dosis",18,'bold'),
                        onvalue=1,
                        offvalue=0,
                        variable=variables_bebidas[contador],
                        command=revisar_check)
    bebidas.grid(row=contador,column=0,sticky=W)
    # crear cuadros de entrada
    
    cuadros_bebidas.append('')
    texto_bebidas.append('')
    texto_bebidas[contador] = StringVar()
    texto_bebidas[contador].set(0)
    cuadros_bebidas[contador] = Entry(panel_bebidas,
                                font=('Dosis',18,'bold'),
                                bd=1,
                                width=6,
                                state=DISABLED,
                                textvariable=texto_bebidas[contador])
    cuadros_bebidas[contador].grid(row=contador,
                                column=1)
    contador += 1


# generar items postres
contador = 0
variables_postres = []
cuadros_postres = []
texto_postres = []
for postres in lista_postres:
    # crear checkbuttons
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postres = Checkbutton(panel_postres,
                        text=postres.title(),
                        font=("Dosis",18,'bold'),
                        onvalue=1,
                        offvalue=0,
                        variable=variables_postres[contador],
                        command= revisar_check)
    postres.grid(row=contador,column=0,sticky=W)
    # crear cuadros de entrada
    
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set(0)
    cuadros_postres[contador] = Entry(panel_postres,
                                font=('Dosis',16,'bold'),
                                bd=1,
                                width=6,
                                state=DISABLED,
                                textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador,
                                column=1)
    contador += 1
    
    
var_costo_comidas = StringVar()
var_costo_bebidas= StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()


# etiquetas de costo y campos de entrada Comida
etiqueta_costo_comida = Label(panel_costos,
                            text="Costo Comida",
                            font=("Dosis",12,"bold"),
                            bg="azure4",
                            fg="white")
etiqueta_costo_comida.grid(row=0,column=0)

texto_costo_comida = Entry(panel_costos,
                        font=("Dosis",12,"bold"),
                        bd=1,
                        width=8,
                        state='readonly',
                        textvariable=var_costo_comidas)
texto_costo_comida.grid(row=0,column=1,padx=41)



# etiquetas de costo y campos de entrada Bebidas
etiqueta_costo_bebidas = Label(panel_costos,
                            text="Costo Bebidas",
                            font=("Dosis",12,"bold"),
                            bg="azure4",
                            fg="white")
etiqueta_costo_bebidas.grid(row=1,column=0)

texto_costo_bebidas = Entry(panel_costos,
                        font=("Dosis",12,"bold"),
                        bd=1,
                        width=8,
                        state='readonly',
                        textvariable=var_costo_bebidas)
texto_costo_bebidas.grid(row=1,column=1,padx=41)




# etiquetas de costo y campos de entrada Postres
etiqueta_costo_postres = Label(panel_costos,
                            text="Costo Postres",
                            font=("Dosis",12,"bold"),
                            bg="azure4",
                            fg="white")
etiqueta_costo_postres.grid(row=2,column=0)

texto_costo_postres = Entry(panel_costos,
                        font=("Dosis",12,"bold"),
                        bd=1,
                        width=8,
                        state='readonly',
                        textvariable=var_costo_postres)
texto_costo_postres.grid(row=2,column=1,padx=41)




# Etiquetas subtotal
etiqueta_subtotal = Label(panel_costos,
                            text="Subtotal",
                            font=("Dosis",12,"bold"),
                            bg="azure4",
                            fg="white")
etiqueta_subtotal.grid(row=0,column=2)

texto_subtotal = Entry(panel_costos,
                        font=("Dosis",12,"bold"),
                        bd=1,
                        width=8,
                        state='readonly',
                        textvariable=var_subtotal)
texto_subtotal.grid(row=0,column=3,padx=41)



# Etiquetas Impuestos
etiqueta_impuesto = Label(panel_costos,
                            text="Impuestos",
                            font=("Dosis",12,"bold"),
                            bg="azure4",
                            fg="white")
etiqueta_impuesto.grid(row=1,column=2)

texto_impuesto = Entry(panel_costos,
                        font=("Dosis",12,"bold"),
                        bd=1,
                        width=8,
                        state='readonly',
                        textvariable=var_impuesto)
texto_impuesto.grid(row=1,column=3,padx=41)

# Etiquetas Total
etiqueta_total = Label(panel_costos,
                            text="Total",
                            font=("Dosis",12,"bold"),
                            bg="azure4",
                            fg="white")
etiqueta_total.grid(row=2,column=2)

texto_total = Entry(panel_costos,
                        font=("Dosis",12,"bold"),
                        bd=1,
                        width=8,
                        state='readonly',
                        textvariable=var_total)
texto_total.grid(row=2,column=3,padx=41)


#botones
botones = ['total','recibo','guardar','resetear']
botones_creados = []


columnas = 0

for boton in botones:
    boton = Button(panel_botones,
                text=boton.title(),
                font=("Dosis",10,"bold"),
                fg="white",
                bg="azure4",
                bd=1,
                width=6)
    botones_creados.append(boton)
    boton.grid(row=0,
                column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)
# area de recibo
texto_recibo = Text(panel_recibo,
                    font=("Dosis",12,"bold"),
                    bd=1,
                    width=35,
                    height=14)
texto_recibo.grid(row=0,column=0)


# Calculadora

visor_calculadora = Entry(panel_calculadora,
                        font=("dosis",10,"bold"),
                        width=40,
                        bd=1)
visor_calculadora.grid(row=0,column=0,columnspan=4,padx=0)

botones_calculadora = ['7','8','9','+','4','5','6',
                '-','1','2','3','x','RES',"DEL",'0',"/"]

botones_guardados = []

fila = 1
columnas = 0

for boton in botones_calculadora:
    boton = Button(
        panel_calculadora,
        text=boton.title(),
        font=("Dosis",10,"bold"),
        fg="white",
        bg="azure4",
        bd=1,
        width=6
    )
    botones_guardados.append(boton)
    boton.grid(row=fila,column=columnas)
    
    if columnas == 3:
        fila += 1
    
    columnas += 1
    
    if columnas == 4:
        columnas = 0
botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))
# Evitar que la aplicacion se cierre
aplicacion.mainloop()
