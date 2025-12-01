from model import cochesBD
from tkinter import messagebox
class Controladores():
    @staticmethod
    def respuesta_sql(titulo,respuesta):
        if respuesta:
            messagebox.showinfo(title=titulo,message="La accion se ha realizado con exito")
        else:
            messagebox.showinfo(title="Algo ha salido mal",message="La accion no se ha podido realizar",icon="warning")
#Parte de coches
    @staticmethod
    def coche_insertar(marca,color,modelo,velocidad,potencia,plazas):
        resultado=cochesBD.Autos.insertar(marca,color,modelo,velocidad,potencia,plazas)
        Controladores.respuesta_sql("Insertar coches",resultado)

    @staticmethod
    def coche_mostrar():
        registro=cochesBD.Autos.consultar()
        return registro
    
    @staticmethod
    def coche_cambiar(marca,color,modelo,velocidad,potencia,plazas,id):
        resultado=cochesBD.Autos.actualizar(marca,color,modelo,velocidad,potencia,plazas,id)
        Controladores.respuesta_sql("Modificar coche",resultado)

    @staticmethod
    def coche_eliminar(id):
        resultado=cochesBD.Autos.eliminar(id)
        Controladores.respuesta_sql("Eliminar un coche", resultado)

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
        resultado=cochesBD.Camionetas.insertar(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
        Controladores.respuesta_sql("Agregar camioneta", resultado)

    @staticmethod
    def camionetas_mostrar():
        registro=cochesBD.Camionetas.consultar()
        return registro

    @staticmethod
    def camioneta_cambiar(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada,id):
        resultado=cochesBD.Camionetas.actualizar(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada,id)
        Controladores.respuesta_sql("Modificar camioneta",resultado)

    @staticmethod
    def camionetas_eliminar(id):
        resultado=cochesBD.Camionetas.eliminar(id)
        Controladores.respuesta_sql("Eliminar una camioneta", resultado)
