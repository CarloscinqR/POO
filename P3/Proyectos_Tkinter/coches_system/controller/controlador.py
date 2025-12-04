from model import cochesBD
from tkinter import messagebox
from view import interfaz
class Controladores():
    @staticmethod
    def insertar_coche(marca,color,modelo,velocidad,potencia,plazas):
        respuesta=cochesBD.Autos.insertar(marca,color,modelo,velocidad,potencia,plazas)
        if respuesta:
            messagebox.showinfo(message="La accion se ha realizado con exito",title="Agregar coche")
        else:
            messagebox.showinfo(message="No se ha podido realizar la accion",title="Ha ocurrido un error",icon="warning")

    @staticmethod
    def mostrar_coche():
        registros=cochesBD.Autos.consultar()
        if len(registros)>0:
            return registros
        else:
            messagebox.showinfo(message="No existe ningun registro por el momento",title="No hay registros",icon="warning")

    @staticmethod
    def actualizar_coche(marca,color,modelo,velocidad,potencia,plazas,id):
        respuesta=cochesBD.Autos.actualizar(marca,color,modelo,velocidad,potencia,plazas,id)
        if respuesta:
            messagebox.showinfo(message=f"Se ha cambiado el coche de id: {id} con exito",title="Modificar coche")
        else:
            messagebox.showinfo(message="No se ha podido realizar la accion",title="Ha ocurrido un error",icon="warning")
    
    @staticmethod
    def eliminar_coche(id):
        respuesta=cochesBD.Autos.eliminar(id)
        if respuesta:
            messagebox.showinfo(message=f"Se ha eliminado el coche de id: {id} con exito",title="Eliminar coche")
        else:
            messagebox.showinfo(message="No se ha podido realizar la accion",title="Ha ocurrido un error",icon="warning")

    @staticmethod
    def buscarId_eliminar(ventana,opid,tipo):
        registro=cochesBD.Autos.consultar()
        for filas in registro:
            if filas[0]==opid:
                if tipo=="coches":
                    interfaz.InterfacesMenu.coches_eliminar(ventana,opid)
                elif tipo=="camionetas":
                    pass
                elif tipo=="camions":
                    pass
                return
            else:
                confirmacion=False
        if confirmacion==False:
            messagebox.showinfo(message="No se encontro el id en registros",title="Ocurrio un problema")

    @staticmethod
    def buscarId_modificar(ventana,opid,tipo):
        registro=cochesBD.Autos.consultar()
        for filas in registro:
            if filas[0]==opid:
                if tipo=="coches":
                    interfaz.InterfacesMenu.coches_cambiar(ventana,opid)
                elif tipo=="camionetas":
                    pass
                elif tipo=="camions":
                    pass
                return
            else:
                confirmacion=False
        if confirmacion==False:
            messagebox.showinfo(message="No se encontro el id en registros",title="Ocurrio un problema")