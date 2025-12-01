from tkinter import *
ventana=Tk()
ventana.title("List box")
ventana.geometry("500x500")

def mostrarEstado():
    color=lbxColor.get(lbxColor.curselection())
    lblNoti.config(text=f"Seleccionaste: {color}")


lbxColor=Listbox(ventana,width=10,height=5,selectmode=SINGLE)
colores=["Amarillo","Rojo","Azul","Morado"]
for i in colores:
    lbxColor.insert(END,i)
lbxColor.pack()

btnConfirmar=Button(ventana,text="Mostrar valor",command=mostrarEstado)
btnConfirmar.pack()

lblNoti=Label(ventana,text="")
lblNoti.pack()

ventana.mainloop()