from tkinter import *
def comentario():
    mensaje=txtCom.get("1.0",END).strip()
    lblMensaje.config(text=f"Comentario: {mensaje}")

ventana=Tk()
ventana.title("Uso del entry")
ventana.geometry("600x400")

lblCom=Label(ventana,
                text="Introduzca su comentario:",
            )
lblCom.pack()

txtCom=Text(ventana,border=2,relief=SOLID)
txtCom.config(width=50,height=6)
txtCom.pack()

btnCom=Button(ventana,text="Mostrar Comentario",command=comentario)
btnCom.pack(pady=10)

lblMensaje=Label(ventana,text="")
lblMensaje.pack()


ventana.mainloop()