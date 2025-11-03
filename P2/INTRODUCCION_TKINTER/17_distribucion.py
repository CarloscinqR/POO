from tkinter import *

ventana=Tk()
ventana.title("Uso del entry")
ventana.geometry("600x400")
#Opcion 1: Con pack() con side=LEFT o RIGHT:
lblUser=Label(ventana,
                text="Introduzca su nombre:",
                )
lblUser.pack(anchor="nw",side=TOP,padx=5,pady=5)

txtNomb=Entry(ventana,width=30)
txtNomb.focus()
txtNomb.pack(anchor="nw",side=TOP,padx=5,pady=5)

lblPass=Label(ventana,
                text="Introduzca su contraseña:",
                )
lblPass.pack(anchor="nw",side=TOP,padx=5,pady=5)

txtPass=Entry(ventana,width=30)
txtPass.pack(anchor="nw",side=TOP,padx=5,pady=5)

#Opcion 2: Con grid():

marco=Frame(ventana,width=600)
marco.pack()

lblUser=Label(marco,
                text="Introduzca su nombre:",
                )
lblUser.grid(row=0,column=0,padx=5,pady=5)

txtNomb=Entry(marco,width=30)
txtNomb.focus()
txtNomb.grid(row=0,column=1,padx=5,pady=5)

lblPass=Label(marco,
                text="Introduzca su contraseña:",
                )
lblPass.grid(row=1,column=0,padx=5,pady=5)

txtPass=Entry(marco,width=30)
txtPass.grid(row=1,column=1,padx=5,pady=5)


ventana.mainloop()