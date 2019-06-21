# Ejercicio Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones para los dígitos 0 al 9
# y las operaciones + - / * = , que al apretar cada botón vaya agregando al valor que muestra en el entry el carácter
# que le corresponde ( como se ve imagen ) y cuando se aprieta en = pone el resultado de evaluar la cadena entrada .

from tkinter import *

from sqlalchemy.orm.sync import clear

ventana=Tk()
ventana.title("Calculadora")
ventana.geometry("375x457")

def bClik(num):
    global var
    var = var+str(num)
    input_text.set(var)

def operacion():
    global var
    try:
        va =str(eval(var))
    except:
        clear()
        va=("ERROR")
    input_text.set(va)

color_boton = "grey"
ancho_boton=6
alto_boton=2
input_text=StringVar()
var=""

def clear():
    global var
    var =("")
    input_text.set("0")


Boton0=Button(ventana,text="0",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:bClik(0)).place(x=20,y=360)
Boton1=Button(ventana,text="1",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:bClik(1)).place(x=20,y=300)
Boton2=Button(ventana,text="2",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:bClik(2)).place(x=113,y=300)
Boton3=Button(ventana,text="3",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:bClik(3)).place(x=207,y=300)
Boton4=Button(ventana,text="4",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:bClik(4)).place(x=20,y=240)
Boton5=Button(ventana,text="5",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:bClik(5)).place(x=113,y=240)
Boton6=Button(ventana,text="6",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:bClik(6)).place(x=207,y=240)
Boton7=Button(ventana,text="7",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:bClik(7)).place(x=20,y=180)
Boton8=Button(ventana,text="8",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:bClik(8)).place(x=113,y=180)
Boton9=Button(ventana,text="9",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:bClik(9)).place(x=207,y=180)
BotonSuma=Button(ventana,text="+",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:bClik("+")).place(x=297,y=180)
BotonResta=Button(ventana,text="-",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:bClik("-")).place(x=297,y=240)
BotonMulti=Button(ventana,text="*",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:bClik("*")).place(x=297,y=300)
BotonDiv=Button(ventana,text="/",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:bClik("/")).place(x=297,y=360)
BotonIgual=Button(ventana,text="=",bg=color_boton,width=ancho_boton+3,height=alto_boton,command=operacion).place(x=194,y=360)
BotonCE=Button(ventana,text="CE",bg=color_boton,width=ancho_boton,height=alto_boton,command=clear).place(x=113,y=360)

Pantalla=Entry(ventana,font=('arial',25,'bold'),textvariable=input_text,justify="right").pack(side="top",ipady=20,pady=30)


ventana.mainloop()
