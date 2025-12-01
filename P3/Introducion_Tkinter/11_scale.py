from tkinter import *
ventana=Tk()
ventana.title("Scale")
ventana.geometry("500x500")

def mostrarEstado():
    lblNoti.config(text=f"Valor seleccionado por el usuario: {valor.get()} ")

valor=IntVar()
scData=Scale(ventana,from_=0,to=100,orient=HORIZONTAL,variable=valor)
scData.pack()

btnConfirmar=Button(ventana,text="Mostrar valor",command=mostrarEstado)
btnConfirmar.pack()

lblNoti=Label(ventana,text="")
lblNoti.pack()


ventana.mainloop()