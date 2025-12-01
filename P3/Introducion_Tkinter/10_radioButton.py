from tkinter import *
ventana=Tk()
ventana.title("Radio button")
ventana.geometry("500x500")

def mostrarEstado():
    lblNoti.config(text=f"Opcion seleccionada: {opcion.get()}")



opcion=StringVar()
rbtnOp1=Radiobutton(ventana,text="Opcion 1",variable=opcion,value="Opcion 1")
rbtnOp1.pack()
rbtnOp2=Radiobutton(ventana,text="Opcion 2",variable=opcion,value="Opcion 2")
rbtnOp2.pack()
rbtnOp3=Radiobutton(ventana,text="Opcion 3",variable=opcion,value="Opcion 3")
rbtnOp3.pack()


btnConfirmar=Button(ventana,text="Mostrar seleccion",command=mostrarEstado)
btnConfirmar.pack()

lblNoti=Label(ventana,text="")
lblNoti.pack()


ventana.mainloop()