#Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones
# 1- un  botón  Alta que inicia otra venta donde puedo ingresar una ciudad y su código postal .
# 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
# 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra .


import tkinter as tk
from tkinter import ttk



class Formulario(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Formulario")
        main_window.geometry("400x320")

        self.treeview = ttk.Treeview(self) #creamos instancia de la clase ttk.Treeview
        #El primer elemento que le pasamos a insert es un ítem o bien una cadena vacía ("") para indicar
        # que el nuevo ítem no tiene predecesor.
        item = self.treeview.insert("", tk.END, text="Rosario")
        self.treeview.insert(item, tk.END, text="2000")
        item = self.treeview.insert("", tk.END, text="Arroyo Seco")
        self.treeview.insert(item, tk.END, text="2128")
        item = self.treeview.insert("", tk.END, text="Funes")
        self.treeview.insert(item, tk.END, text="2132")
        item = self.treeview.insert("", tk.END, text="Villa Constitución")
        self.treeview.insert(item, tk.END, text="2919")
        item = self.treeview.insert("", tk.END, text="San Lorenzo")
        self.treeview.insert(item, tk.END, text="2200")
        self.treeview.pack()

        self.pack()


main_window = tk.Tk()
form = Formulario(main_window)

#Alta
def formulario_alta():
    new_ventana = tk.Toplevel(main_window)
    main_window.iconify() #minimiza la ventana principal
    var_ciudad = tk.StringVar()
    var_CP = tk.StringVar()
    label = tk.Label(new_ventana, text="Ciudad: ")
    label2 = tk.Label(new_ventana, text="Código Postal: ")
    label.grid(column=1, row=1, padx=(50,50), pady=(10,10))
    label2.grid(column=2, row=1, padx=(40,40), pady=(10,5))


    Ciudad = tk.Entry(new_ventana,textvariable=var_ciudad)
    Ciudad.grid(column=1, row=2, padx=(5,5), pady=(10,5))
    CP = tk.Entry(new_ventana,textvariable=var_CP)
    CP.grid(column=2, row=2, padx=(5,5), pady=(10,5))

    btn_alta = tk.Button(new_ventana, text="Añadir")
    btn_alta.grid(column=3, row=2, padx=(50,50), pady=(10,10))
    def alta(event):
        item = form.treeview.insert("", tk.END, text=Ciudad.get())
        form.treeview.insert(item, tk.END, text=CP.get())
        main_window.deiconify()

    btn_alta.bind("<Button-1>", alta)

btn_frm_alta = tk.Button(main_window, bg='green', text="ALTA", command=formulario_alta)
btn_frm_alta.pack()



#Baja
def baja():
    dev_item = form.treeview.focus() #trae el elemento que está seleccionado
    form.treeview.delete(dev_item)
btn_baja = tk.Button(main_window, bg='red', text="BAJA", command=baja)
btn_baja.pack()


#Modificacion
def formulario_modificacion():
    new_ventana = tk.Toplevel(main_window)
    main_window.iconify()
    elem = form.treeview.focus()
    elem_child = form.treeview.get_children(elem)
    var_ciudad = tk.StringVar(new_ventana, value=form.treeview.item(elem)['text'])

    var_CP = tk.StringVar(new_ventana, value=form.treeview.item(elem_child)['text'])
    label = tk.Label(new_ventana, text="Ciudad: ")
    label2 = tk.Label(new_ventana, text="Código Postal: ")
    label.grid(column=1, row=1, padx=(50,50), pady=(10,10))
    label2.grid(column=2, row=1, padx=(40,40), pady=(10,5))


    Ciudad = tk.Entry(new_ventana,textvariable=var_ciudad)
    Ciudad.grid(column=1, row=2, padx=(5,5), pady=(10,5))
    CP = tk.Entry(new_ventana,textvariable=var_CP)
    CP.grid(column=2, row=2, padx=(5,5), pady=(10,5))

    btn_alta = tk.Button(new_ventana, text="Modificar")
    btn_alta.grid(column=3, row=2, padx=(50,50), pady=(10,10))
    def modificacion(event):
        form.treeview.item(elem,text=Ciudad.get())
        form.treeview.item(elem_child,text=CP.get())
        main_window.deiconify()

    btn_alta.bind("<Button-1>", modificacion)

btn_frm_alta = tk.Button(main_window, bg='yellow', text="MODIFICAR", command=formulario_modificacion)
btn_frm_alta.pack()

form.mainloop()
