from model import cochesBD
from tkinter import messagebox
from view import interfaz
class Controladores():
#PARTE DE COCHES

    @staticmethod
    def respuesta_sql(titulo,resultado):
        if resultado:
            messagebox.showinfo(message="La accion se ha realizado con exito",title=titulo)
        else:
            messagebox.showinfo(message="No se ha podido realizar la accion",title="Ha ocurrido un error",icon="warning")

    @staticmethod
    def insertar_coche(marca,color,modelo,velocidad,potencia,plazas):
        respuesta=cochesBD.Autos.insertar(marca,color,modelo,velocidad,potencia,plazas)
        Controladores.respuesta_sql("Agregar coche",respuesta)

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
        Controladores.respuesta_sql("Modificar coche",respuesta)
    
    @staticmethod
    def eliminar_coche(id):
        respuesta=cochesBD.Autos.eliminar(id)
        Controladores.respuesta_sql("Eliminar coche",respuesta)

#Parte de camiones
    @staticmethod
    def camion_insertar(marca,color,modelo,velocidad,potencia,plazas,eje,capacidad):
        resultado=cochesBD.Camiones.insertar(marca,color,modelo,velocidad,potencia,plazas,eje,capacidad)
        Controladores.respuesta_sql("Agregar camion",resultado)

    @staticmethod
    def camion_mostrar():
        registro=cochesBD.Camiones.consultar()
        return registro

    @staticmethod
    def camion_cambiar(marca,color,modelo,velocidad,potencia,plazas,eje,capacidad,id):
        resultado=cochesBD.Camiones.actualizar(marca,color,modelo,velocidad,potencia,plazas,eje,capacidad,id)
        Controladores.respuesta_sql("Modificar camion",resultado)

    @staticmethod
    def camion_eliminar(id):
        resultado=cochesBD.Camiones.eliminar(id)
        Controladores.respuesta_sql("Eliminar un camion", resultado)

#Parte de camionetas
    @staticmethod
    def camionetas_insertar(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada):
        if cerrada=="Si":
            cerrada=1
        else:
            cerrada=0
        resultado=cochesBD.Camionetas.insertar(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
        Controladores.respuesta_sql("Agregar camioneta", resultado)

    @staticmethod
    def camionetas_mostrar():
        registro=cochesBD.Camionetas.consultar()
        return registro

    @staticmethod
    def camioneta_cambiar(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada,id):
        if cerrada=="Si":
            cerrada=1
        else:
            cerrada=0
        resultado=cochesBD.Camionetas.actualizar(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada,id)
        Controladores.respuesta_sql("Modificar camioneta",resultado)

    @staticmethod
    def camionetas_eliminar(id):
        resultado=cochesBD.Camionetas.eliminar(id)
        Controladores.respuesta_sql("Eliminar una camioneta", resultado)








    @staticmethod
    def buscarId_eliminar(ventana,opid,tipo):
        if tipo=="coches":
            registro=cochesBD.Camiones.consultar()
        elif tipo=="camionetas":
            registro=cochesBD.Camionetas.consultar()
        elif tipo=="camiones":
            registro=cochesBD.Camiones.consultar()
        for filas in registro:
            if filas[0]==opid:
                if tipo=="coches":
                    interfaz.InterfacesMenu.coches_eliminar(ventana,opid)
                elif tipo=="camionetas":
                    interfaz.InterfacesMenu.camionetas_eliminar(ventana,opid)
                elif tipo=="camiones":
                    interfaz.InterfacesMenu.camiones_eliminar(ventana,opid)
                return
            else:
                confirmacion=False
        if confirmacion==False:
            messagebox.showinfo(message="No se encontro el id en registros",title="Ocurrio un problema")

    @staticmethod
    def buscarId_modificar(ventana,opid,tipo):
        if tipo=="coches":
            registro=cochesBD.Camiones.consultar()
        elif tipo=="camionetas":
            registro=cochesBD.Camionetas.consultar()
        elif tipo=="camiones":
            registro=cochesBD.Camiones.consultar()
        
        for filas in registro:
            if filas[0]==opid:
                if tipo=="coches":
                    interfaz.InterfacesMenu.coches_cambiar(ventana,opid)
                elif tipo=="camionetas":
                    interfaz.InterfacesMenu.camionetas_cambiar(ventana,opid)
                elif tipo=="camiones":
                    interfaz.InterfacesMenu.camiones_cambiar(ventana,opid)
                return
            else:
                confirmacion=False
        if confirmacion==False:
            messagebox.showinfo(message="No se encontro el id en registros",title="Ocurrio un problema")