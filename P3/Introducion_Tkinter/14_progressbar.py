from tkinter import *
from tkinter import ttk
ventana=Tk()
ventana.title("Progress bar")
ventana.geometry("500x500")

def progreso():
    bpProgreso['value']=0
    ventana.update()
    for i in range(101):
        bpProgreso["value"]=i
        ventana.update()
        ventana.after(50)

bpProgreso=ttk.Progressbar(ventana,mode="determinate",length=200)
bpProgreso.pack()

btnConfirmar=Button(ventana,text="Iniciar progreso",command=progreso)
btnConfirmar.pack()

ventana.mainloop()