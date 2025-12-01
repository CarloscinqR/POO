from tkinter import messagebox
from model import operaciones
from view import interfaz
class Controladores():
    @staticmethod
    def operacion(a,b,op,caracter):
        match op:
            case "suma":
                opera=a+b 
            case "resta":
                opera=a-b
            case "multiplicacion":
                opera=a*b
            case "division":
                opera=a/b
        #messagebox.showinfo(message=f"El resultado de {a} {caracter} {b} es: {opera}",title=op)
        respuesta=messagebox.askquestion(message=f"{a} {caracter} {b} es: {opera}\nQuieres insertarlo en la base de datos").lower()
        if respuesta=="yes":
            Controladores.respuesta_sql("Agregar Registro",operaciones.Operaciones.crear(a,b,caracter,opera))

    @staticmethod
    def mostrar():
        datos=operaciones.Operaciones.mostrar()
        if len(datos)>0:
            n_op=0
            show=[]
            for filas in datos:
                show.append(f"Operacion {n_op+1} ID{filas[0]} Fecha de creacion {filas[1]}\nOperacion {filas[2]} {filas[4]} {filas[3]} = {filas[5]}\n")
                n_op+=1
            texto_final="".join(show)
            return texto_final
        else:
            messagebox.showinfo(message="No hay registros en la tabla")     

    @staticmethod
    def respuesta_sql(titulo,respuesta):
        if respuesta:
            messagebox.showinfo(title=titulo,message="La accion se ha realizado con exito")
        else:
            messagebox.showinfo(title="Algo ha salido mal",message="La accion no se ha podido realizar",icon="warning")
    
    @staticmethod
    def buscarId(ventana,opid):
        registro=operaciones.Operaciones.mostrar()
        for filas in registro:
            print(filas[0])
            print(opid)
            if filas[0]==opid:
                interfaz.Vistas.interfazEliminar(ventana,opid)
                return
            else:
                confirmacion=False
        if confirmacion==False:
            messagebox.showinfo(message="No se encontro el id en registros",title="Ocurrio un problema")
        
            