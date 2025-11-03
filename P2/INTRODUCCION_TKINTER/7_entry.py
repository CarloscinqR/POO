'''
from tkinter import *
def clickarSaludar():
    lblSaludo.config(text=f"Hola,bienvenido {nombre.get()}")

ventana=Tk()
ventana.title("Uso del entry")
ventana.geometry("400x600")

lblTitulo=Label(ventana,text="Ingrese su nombre:")
lblTitulo.pack()

nombre=StringVar()

txtNomb=Entry(ventana,width=30,textvariable=nombre)
txtNomb.pack()

btnSaludar=Button(ventana,text="Saludar",command=clickarSaludar)
btnSaludar.pack()

lblSaludo=Label(ventana,text="")
lblSaludo.pack()


ventana.mainloop()
'''
from tkinter import *


def salir():
    ventana.quit()

def ingresar():
    usuario=txtNomb.get()
    password=txtPass.get()
    if len(password)>0:
        lblMens.config(text=f"Bienvenido {usuario}")
        txtNomb.config(state="readonly")
        txtPass.config(state="readonly")
    else:
        lblMens.config(text="Debe de ingresar una contraseña")
def borrar():
    txtNomb.config(state="normal")
    txtPass.config(state="normal")
    txtNomb.focus()
    txtNomb.delete(0,END)
    txtPass.delete(0,END)
    lblMens.destroy()


    '''
    color_defecto = ventana.cget("bg")
    lblMens.config(text="",
                font=("Comic Sans MS",12),
                width=20,
                background=color_defecto
                )
    '''

ventana=Tk()
ventana.title("Uso del entry")
ventana.geometry("800x600")
ventana.config(background="lightgray")

lblTitulo=Label(ventana,
                text="Ingreso al sistema",
                font=("Comic Sans MS",18),
                background="#D52F53",
                width=400,
                height=5
                )
lblTitulo.pack()
marco=Frame(ventana)
marco.config(height=200,width=800,background="lightgray")
marco.pack_propagate(False)
marco.pack()

lblUser=Label(marco,
                text="Introduzca su usario:",
                font=("Comic Sans MS",12),
                background="#D52F53",
                width=20
                )
lblUser.grid(row=0,column=0,padx=5,pady=5)

txtNomb=Entry(marco,width=30)
txtNomb.focus()
txtNomb.grid(row=0,column=1,padx=5,pady=5)

lblPass=Label(marco,
                text="Introduzca su contraseña",
                font=("Comic Sans MS",12),
                background="#D52F53",
                width=20
                )
lblPass.grid(row=1,column=0,padx=5,pady=5)

txtPass=Entry(marco,width=30,show="*")
txtPass.grid(row=1,column=1,padx=5,pady=5)

marcoBtn=Frame(ventana,background="lightgray")
marcoBtn.pack_propagate(False)
marcoBtn.pack()

btnIng=Button(marcoBtn,text="Ingresar",font=("Comic Sans MS",12),command=ingresar)
btnIng.grid(row=2,column=0,padx=5,pady=5)
btnBorrar=Button(marcoBtn,text="Borrar",font=("Comic Sans MS",12),command=borrar)
btnBorrar.grid(row=2,column=1,padx=5,pady=5)
btnSalir=Button(marcoBtn,text="Salir",font=("Comic Sans MS",12),command=salir)
btnSalir.grid(row=2,column=2,padx=5,pady=5)

lblMens=Label(ventana,
                text="",
                font=("Comic Sans MS",10),
                width=40,
                background="lightgray"
                )
lblMens.pack()

ventana.mainloop()


