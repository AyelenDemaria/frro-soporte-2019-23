#Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
# Ciudades Argentinas y su código postal ( por lo menos 5 ciudades ) .

import tkinter as tk
from tkinter import ttk



class Formulario(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Formulario")
        main_window.geometry("250x200")

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
Formulario(main_window).mainloop()

