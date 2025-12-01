from tkinter import *
import os
#pip install --upgrade pillow
#pip install --upgrade pip

ventana=Tk()
ventana.title("Imagenes pillow")
ventana.geometry("500x500")

def mensaje(tipo):
    lblResultado.config(text=tipo)

#1er de agregar imagenes con la libreria de tkinter ya incluidas
#PhotoImage solo permite archivos con extension .png .gif .
ruta_base = os.path.dirname(os.path.abspath(__file__))
ruta_imagen = os.path.join(ruta_base, "image\logo_utd.png")
imagen=PhotoImage(file=ruta_imagen)

#Imagen con pil
'''
img=Image.open(ruta_imagen)
img=img.resize((100,100))
imagen_tk=ImagenTk.PhotoImage(img)
'''

lblImagen=Label(ventana,image=imagen,text="Somos buffalos.... UTD",compound=TOP)
lblImagen.pack()

boton=Button(ventana,image=imagen,command=lambda: mensaje("Hola python"))
boton.pack()
lblResultado=Label(ventana,text="")
lblResultado.pack()

ventana.mainloop()