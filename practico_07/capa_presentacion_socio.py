from tkinter import ttk
from tkinter import *
from practico_06.capa_negocio import NegocioSocio
from practico_05.ejercicio_01 import Socio


class Capa_presentacion_socio:


    def __init__(self, window):

        self.wind = window
        self.wind.title('Gestion Socios')


        frame = LabelFrame(self.wind, text = 'Nuevo Socio')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # dni Input
        Label(frame, text = 'DNI: ').grid(row = 1, column = 0)
        self.dni = Entry(frame)
        self.dni.focus()
        self.dni.grid(row = 1, column = 1)

        # Nombre Input
        Label(frame, text = 'Nombre: ').grid(row = 2, column = 0)
        self.nombre = Entry(frame)
        self.nombre.grid(row = 2, column = 1)

        # Apellido Input
        Label(frame, text = 'Apellido: ').grid(row = 3, column = 0)
        self.apellido = Entry(frame)
        self.apellido.grid(row = 3, column = 1)

        # Button Agregar Socio
        ttk.Button(frame, text = 'Registrar Socio', command = self.alta_socio).grid(row = 4, columnspan = 2, sticky = W + E)

        # Output Messages
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 4, column = 0, columnspan = 2, sticky = W + E)

        # Table
        self.tree = ttk.Treeview(height = 10, columns = ("#1","#2"))
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'DNI', anchor = CENTER)
        self.tree.heading('#1', text = 'Nombre', anchor = CENTER)
        self.tree.heading('#2', text = 'Apellido', anchor = CENTER)

        # Buttons
        ttk.Button(text = 'ELIMINAR', command = self.baja_socio).grid(row = 5, column = 0, sticky = W + E)
        ttk.Button(text = 'MODIFICAR', command = self.modificar_socio).grid(row = 5, column = 1, sticky = W + E)


        self.get_socios()

    def get_socios(self):
        # cleaning Table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # traemos todos los socios
        ns = NegocioSocio()
        socios = ns.todos()


        for row in socios:
            self.tree.insert('', 0, text = row.dni, values = [row.nombre, row.apellido])



    def alta_socio(self):
            socio = Socio(dni=self.dni.get(), nombre=self.nombre.get(), apellido=self.apellido.get())
            ns = NegocioSocio()
            ns.alta(socio)
            self.dni.delete(0, END)
            self.nombre.delete(0, END)
            self.apellido.delete(0, END)

            self.get_socios()

    def baja_socio(self):
        dni = self.tree.item(self.tree.selection())['text']
        ns = NegocioSocio()
        socio_1 = ns.buscar_dni(dni)
        ns.baja(socio_1.id_socio)
        self.get_socios()

    def modificar_socio(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'Please, select Record'
            return
        dni_old = self.tree.item(self.tree.selection())['text']
        old_name = self.tree.item(self.tree.selection())['values'][0]
        old_surname = self.tree.item(self.tree.selection())['values'][1]
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Editar Socio'

        Label(self.edit_wind, text = 'DNI: ').grid(row = 0, column = 1)
        new_dni = Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = dni_old))
        new_dni.grid(row = 0, column = 2)


        Label(self.edit_wind, text = 'Nombre: ').grid(row = 1, column = 1)
        new_name= Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_name))
        new_name.grid(row = 1, column = 2)


        Label(self.edit_wind, text = 'Apellido: ').grid(row = 2, column = 1)
        new_surname = Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_surname))
        new_surname.grid(row = 2, column = 2)


        Button(self.edit_wind, text = 'Update', command = lambda: self.editar_registros(new_dni.get(), dni_old, new_name.get(), new_surname.get())).grid(row = 3, column = 2, sticky = W)
        self.edit_wind.mainloop()

    def editar_registros(self, new_dni, dni_old, new_name, new_surname):
        ns = NegocioSocio()
        soc = ns.buscar_dni(dni_old)
        soc.nombre = new_name
        soc.apellido = new_surname
        soc.dni = new_dni
        ns.modificacion(soc)
        self.edit_wind.destroy()
        self.get_socios()

if __name__ == '__main__':
    window = Tk()
    application = Capa_presentacion_socio(window)
    window.mainloop()
