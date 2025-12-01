from tkinter import *
ventana=Tk()
ventana.title("Menu")
ventana.geometry("500x500")

def mostrarEstado(texto):
    lblNoti.config(text=f"{texto}")

mnBar=Menu(ventana)#Crea la barra de menu
ventana.config(menu=mnBar)


 
archivoMenu=Menu(mnBar,tearoff=FALSE)#Crea una opcion para el menu
mnBar.add_cascade(label="Archivo",menu=archivoMenu)#Añade la opcion al menu
archivoMenu.add_command(label="Nuevo archivo",command=lambda: mostrarEstado("Nuevo archivo"))#Añade una opcion a la opcion archivo
archivoMenu.add_command(label="Guardar archivo",command=lambda: mostrarEstado("Guardar archivo"))#Añade una opcion a la opcion archivo
archivoMenu.add_separator()#Añade un separador 
archivoMenu.add_command(label="Salir",command=ventana.quit)

editarMenu=Menu(mnBar,tearoff=FALSE)
mnBar.add_cascade(label="Editar",menu=editarMenu)
editarMenu.add_command(label="Copiar",command=lambda: mostrarEstado("Copiar"))
editarMenu.add_command(label="Recortar", command=lambda: mostrarEstado("Recortar"))
editarMenu.add_separator()
editarMenu.add_command(label="Salir", command=ventana.quit,background="#FF0000",foreground="#FFFFFF")

lblNoti=Label(ventana,text="")
lblNoti.pack()



ventana.mainloop()