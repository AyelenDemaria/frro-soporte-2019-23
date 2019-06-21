#1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
# Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
# al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 .

import tkinter as Tk


ventana = Tk.Tk()
ventana.title('Calculadora')
ventana.geometry("400x150")


def cerrar():
    ventana.destroy()
    ventana.quit()
ventana.protocol("WM_DELETE_WINDOW", cerrar)

label1 = Tk.Label(text="Primer operador")
label1.grid(row=0,column=0, padx=5, pady=5)
label2 = Tk.Label(text="Segundo operador")
label2.grid(row=0,column=1,  padx=5, pady=5)

var1 = Tk.DoubleVar()
var1.set('')
var2 = Tk.DoubleVar()
var2.set('')
res = Tk.DoubleVar()

entry1 = Tk.Entry(textvariable = var1)
entry1.grid(row=1,column=0, padx=5, pady=5)
entry2 = Tk.Entry(textvariable = var2)
entry2.grid(row=1,column=1, padx=5, pady=5)

btn_mas = Tk.Button(ventana, text="+")
def sumar(event):
    try:
        res.set(var1.get() + var2.get())
        var1.set('')
        var2.set('')
        print(res.get())
        lbl_res['text'] = res.get() #permite cambiar atributos mientras está corriendo
    except:
         lbl_res['text'] = 'Error'
btn_mas.bind("<Button-1>", sumar)

btn_menos = Tk.Button(ventana, text="-")
def restar(event):
    try:
        res.set(var1.get() - var2.get())
        var1.set('')
        var2.set('')
        print(res.get())
        lbl_res['text'] = res.get()
    except:
         lbl_res['text'] = 'Error'
btn_menos.bind("<Button-1>", restar)


btn_por = Tk.Button(ventana, text="*")
def multiplicar(event):
    try:
        res.set(var1.get() * var2.get())
        var1.set('')
        var2.set('')
        print(res.get())
        lbl_res['text'] = res.get()
    except:
         lbl_res['text'] = 'Error'
btn_por.bind("<Button-1>", multiplicar)


btn_div = Tk.Button(ventana, text="/")
def dividir(event):
    try:
        res.set(var1.get() / var2.get())
        var1.set('')
        var2.set('')
        print(res.get())
        lbl_res['text'] = res.get()
    except:
         lbl_res['text'] = 'Error'
btn_div.bind("<Button-1>", dividir)

lbl_res = Tk.Label(ventana, text=res.get())



btn_mas.grid(column=3, row=1, padx=5, pady=5)
btn_menos.grid(column=4, row=1, padx=5, pady=5)
btn_por.grid(column=5, row=1, padx=5, pady=5)
btn_div.grid(column=6, row=1, padx=5, pady=5)
lbl_res.grid(column=3, row=2, padx=5, pady=5)



ventana.mainloop()
