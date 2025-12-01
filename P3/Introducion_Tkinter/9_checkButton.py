from tkinter import *
ventana=Tk()
ventana.title("Check button")
ventana.geometry("500x500")

def mostrarEstado():
    
    if opcion.get()==1:
        lblNoti.config(text="Notificaciones Activadas")
    elif opcion.get()==0:
        lblNoti.config(text="Notificaciones desctivadas")

opcion=IntVar()
chkbtnNoti=Checkbutton(ventana,text="Desea recibir notficaciones?",variable=opcion,onvalue=1,offvalue=0)
chkbtnNoti.pack()

btnConfirmar=Button(ventana,text="Confirmar",command=mostrarEstado)
btnConfirmar.pack()

lblNoti=Label(ventana,text="")
lblNoti.pack()

ventana.mainloop()